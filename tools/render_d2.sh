#!/usr/bin/env bash
set -euo pipefail

mkdir -p docs/_static/diagrams

find zshooter-too/views -name '*.d2' | while read -r f; do
  base="$(basename "${f%.d2}")"
  d2 --layout elk "$f" "docs/_static/diagrams/${base}.svg"
done

find zshooter-arch/views -name '*.d2' | while read -r f; do
  base="$(basename "${f%.d2}")"
  d2 --layout elk "$f" "docs/_static/diagrams/${base}.svg"
done