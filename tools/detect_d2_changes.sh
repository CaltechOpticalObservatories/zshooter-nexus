#!/usr/bin/env bash
set -euo pipefail

event_name="${1:-}"
before_sha="${2:-}"
after_sha="${3:-}"

if [[ -z "$event_name" && -z "$before_sha" && -z "$after_sha" ]]; then
  event_name="push"
  after_sha="$(git rev-parse HEAD)"
  before_sha="$(git rev-parse HEAD^)"
fi

if [[ -z "$event_name" || -z "$after_sha" ]]; then
  echo "usage: $0 <event_name> <before_sha> <after_sha>" >&2
  echo "       $0    # defaults to comparing HEAD^..HEAD as a push event" >&2
  exit 2
fi

render=false
reasons=()

append_output() {
  local key="$1"
  local value="$2"
  if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
    printf '%s=%s\n' "$key" "$value" >> "$GITHUB_OUTPUT"
  else
    printf '%s=%s\n' "$key" "$value"
  fi
}

ensure_submodule_commit() {
  local path="$1"
  local sha="$2"

  if git -C "$path" cat-file -e "${sha}^{commit}" 2>/dev/null; then
    return 0
  fi

  git -C "$path" fetch --depth=1 origin "$sha" >/dev/null 2>&1
}

git_tree_mode() {
  local path="$1"
  local treeish="$2"

  git ls-tree "$treeish" "$path" | awk '{print $1}'
}

git_tree_sha() {
  local path="$1"
  local treeish="$2"

  git ls-tree "$treeish" "$path" | awk '{print $3}'
}

is_submodule_path() {
  local path="$1"
  local mode

  mode="$(git_tree_mode "$path" "$after_sha")"
  if [[ -z "$mode" ]]; then
    mode="$(git_tree_mode "$path" "$before_sha")"
  fi

  [[ "$mode" == "160000" ]]
}

has_repo_d2_changes() {
  local path="$1"

  git diff --name-only "$before_sha" "$after_sha" -- "$path/views" | grep -E '\.d2$' >/dev/null
}

has_submodule_d2_changes() {
  local path="$1"
  local old_sha
  local new_sha

  old_sha="$(git_tree_sha "$path" "$before_sha")"
  new_sha="$(git_tree_sha "$path" "$after_sha")"

  if [[ -z "$old_sha" || -z "$new_sha" ]]; then
    return 1
  fi

  if [[ "$old_sha" == "$new_sha" ]]; then
    return 1
  fi

  ensure_submodule_commit "$path" "$old_sha"
  ensure_submodule_commit "$path" "$new_sha"

  git -C "$path" diff --name-only "$old_sha" "$new_sha" -- views | grep -E '\.d2$' >/dev/null
}

has_d2_changes() {
  local path="$1"

  if is_submodule_path "$path"; then
    has_submodule_d2_changes "$path"
    return
  fi

  has_repo_d2_changes "$path"
}

if [[ "$event_name" == "push" ]]; then
  if [[ -z "$before_sha" || "$before_sha" == "0000000000000000000000000000000000000000" ]]; then
    render=true
    reasons+=("push has no usable before SHA")
  else
    if git diff --name-only "$before_sha" "$after_sha" -- tools/render_d2.sh tools/detect_d2_changes.sh | grep -q .; then
      render=true
      reasons+=("D2 tooling changed")
    fi

    if has_d2_changes "zshooter-arch"; then
      render=true
      reasons+=("zshooter-arch views/*.d2 changed")
    fi

    if has_d2_changes "zshooter-too"; then
      render=true
      reasons+=("zshooter-too views/*.d2 changed")
    fi
  fi
fi

if [[ "$render" == "true" ]]; then
  append_output "render" "true"
  append_output "reason" "${reasons[*]}"
  echo "D2 render required: ${reasons[*]}"
else
  append_output "render" "false"
  append_output "reason" "copy prebuilt SVGs only"
  echo "D2 render not required. Copying prebuilt SVGs only."
fi
