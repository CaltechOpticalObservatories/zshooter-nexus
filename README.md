# ZShooter site prototype 

## Whats where

- `docs/`:
  - rst source tree
  - CAD/PDF wrappers in `_static/`
  - site stylesheet in `_static/css`
  - `_static/o3dv/` and `_static/pdfjs/` for 3d viewing and pdf viewing
- `tools/`:
  - `generate_cad_manifest.py` for build/stage-time manifest generation
  - `render_d2.sh` for rendering D2 models into submodule `svg/` artifact folders
  - `sync_d2_svgs.sh` for copying prebuilt diagram SVGs into `docs/_static/d2_diagrams`
  - `stage_site.py` for staging ics/drp documentation into the site for deployment

## Current assumptions
- Repo-local CAD assets are assumed to be served relative to the wrappers at `../cad`
- Remote CAD assets are crawled from online server specified in `tools/generate_cad_manifest.py`
- Repo-local `cad/` is copied into the HTML build as `docs/_build/html/cad` by a Sphinx `build-finished` hook in `docs/conf.py`
- Manifest generator run from repo directory
   - `python tools/generate_cad_manifest.py --cad-root ./cad --docs-root ./docs --web-root ../cad`
- The generated manifests merge repo-local `cad/` files with the remote `drawings/` and `solids/` listings.


## Development

```bash
git clone git@github.com:baileyji/zshooter.git
cd zshooter
git submodule update --init --recursive

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

curl -fsSL https://d2lang.com/install.sh | sh -s --
pip install -r requirements.txt

python tools/stage_site.py
python tools/generate_cad_manifest.py --cad-root ./cad --docs-root ./docs --web-root ../cad
bash tools/sync_d2_svgs.sh
python tools/generate_diagram_manifest.py

# Only needed when D2 sources changed and you want to regenerate the committed SVG artifacts.
bash tools/render_d2.sh

sphinx-build -b html docs docs/_build/html

python -m http.server -d docs/_build/html 8000
```
