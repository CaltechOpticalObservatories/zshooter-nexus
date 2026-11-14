#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
python3 tools/render_d2.py "$@"
bash tools/sync_d2_svgs.sh
python3 tools/generate_diagram_manifest.py
