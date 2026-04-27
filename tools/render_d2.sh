#!/usr/bin/env bash
set -euo pipefail

render_tree() {
  local src_root="$1"
  local dst_root="$2"

  mkdir -p "$dst_root"

  find "$src_root" -name '*.d2' | while read -r f; do
    local base
    base="$(basename "${f%.d2}")"
    d2 --layout elk "$f" "$dst_root/${base}.svg"
  done
}

render_tree "zshooter-too/views" "zshooter-too/svg"
render_tree "zshooter-arch/views" "zshooter-arch/svg"

bash tools/sync_d2_svgs.sh
