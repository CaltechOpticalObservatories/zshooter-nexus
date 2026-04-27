#!/usr/bin/env bash
set -euo pipefail

if git diff --quiet -- zshooter-arch/svg zshooter-too/svg; then
  echo "Rendered D2 SVGs match committed artifacts."
  exit 0
fi

echo "::warning::Rendered D2 SVGs differ from committed artifacts."
git --no-pager diff -- zshooter-arch/svg zshooter-too/svg || true
