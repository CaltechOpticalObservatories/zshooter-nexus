#!/usr/bin/env bash
set -euo pipefail

drift=false

if [[ -n "$(git -C zshooter-arch status --porcelain -- svg)" ]]; then
  drift=true
  echo "::warning::Rendered zshooter-arch SVGs differ from committed artifacts."
  git -C zshooter-arch status --short -- svg
  git -C zshooter-arch --no-pager diff -- svg || true
fi

if [[ -n "$(git status --porcelain -- zshooter-too/svg)" ]]; then
  drift=true
  echo "::warning::Rendered zshooter-too SVGs differ from committed artifacts."
  git status --short -- zshooter-too/svg
  git --no-pager diff -- zshooter-too/svg || true
fi

if [[ "$drift" == "false" ]]; then
  echo "Rendered D2 SVGs match committed artifacts."
fi
