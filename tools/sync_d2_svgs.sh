#!/usr/bin/env bash
set -euo pipefail

dst_root="docs/_static/d2_diagrams"

rm -rf "$dst_root"
mkdir -p "$dst_root"

find zshooter-arch/svg -maxdepth 1 -type f -name '*.svg' -exec cp {} "$dst_root"/ \;
find zshooter-too/svg -maxdepth 1 -type f -name '*.svg' -exec cp {} "$dst_root"/ \;
