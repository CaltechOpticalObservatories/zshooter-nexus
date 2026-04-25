# ZShooter site prototype 

## Whats where

- `docs/`:
  - rst source tree
  - CAD/PDF wrappers in `_static/`
  - site stylesheet in `_static/css`
  - `_static/o3dv/` and `_static/pdfjs/` for 3d viewing and pdf viewing
- `tools/`:
  - `generate_cad_manifest.py` for build/stage-time manifest generation
  - `render_d2.sh` for rendering D2 models
  - `stage_site.py` for staging ics/drp documentation into the site for deployment

## Current assumptions
- CAD assets assumed to be served at `/cad` (or equivalent same-origin sibling path)
- `html_extra_path = ["../cad"]` not used as it would cause copy of large files in to build
- Manifest generator run from repo directory
   - `python tools/generate_cad_manifest.py --cad-root ./cad --docs-root ./docs --web-root /cad`
- Symlink created to the CAD tree in web root.


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
python tools/generate_cad_manifest.py --cad-root ./cad --docs-root ./docs --web-root /cad
bash tools/render_d2.sh

sphinx-build -b html docs docs/_build/html
ln -s ../../../cad ./docs/_build/html/cad

python -m http.server -d docs/_build/html 8000
```


