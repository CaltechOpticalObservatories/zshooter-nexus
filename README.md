# ZShooter documentation nexus

This repository builds the ZShooter instrument website and collects the
project's public and team-facing documentation in one navigable site. The
internal/external mode switch is a presentation aid, not access control.

## What's where

- `docs/`:
  - Sphinx source tree (reStructuredText and MyST Markdown)
  - `cad_manifest.json` for optional CAD dropdown labels and ordering
  - eDrawings/PDF directory viewers in `_static/`
  - site stylesheet in `_static/css`
  - `_static/pdfjs/` for PDF viewing
- `tools/`:
  - `render_d2.sh` for rendering D2 models into submodule `svg/` artifact folders
  - `sync_d2_svgs.sh` for copying prebuilt diagram SVGs into `docs/_static/d2_diagrams`
  - `stage_site.py` for composing subproject documentation and notebooks into the site
  - `validate_site.py` for checking required integrated pages and their Sphinx warnings

## Documentation ownership

| Owner | Canonical source | Generated nexus destination | Nexus landing page |
| --- | --- | --- | --- |
| ICS | `zshooter-ics/docs/source/` | `docs/_staged/ics/` | Technical Design → Controlling ZShooter |
| DRP | `zshooter-drp/docs/source/` and `zshooter-drp/notebooks/` | `docs/_staged/drp/` | Observing → Data Reduction |
| Simulator | `zshooter-sim/notebooks/` | `docs/_staged/sim/notebooks/` | Observing → Instrument Simulator |

The generated `_staged` tree is ignored by Git. Edit documentation only in its
canonical repository. Submodule revisions are deliberately pinned: update and
review a submodule gitlink in this repository when its documentation should be
published by the nexus.

## Current assumptions

- CAD
  - `docs/cad.rst` embeds separate eDrawings and PDF viewers.
  - Both viewers discover files recursively from `https://meridian.caltech.edu/`; CAD assets are not mirrored in this
    repository.
  - `docs/cad_manifest.json` can place discovered files first and give them friendlier dropdown labels. Each entry has
    only `file` and `label`; blank labels and unlisted files display their filenames. The manifest is copied by Sphinx
    and has no generation step.
  - The CAD server must expose an HTML directory index and allow browser reads from the docs origin with
    `Access-Control-Allow-Origin`.
  - The wrappers support `cadRoot` overrides plus `selected`, `edrawing`, and `pdf` deep links.



## Development

```bash
git clone git@github.com:CaltechOpticalObservatories/zshooter-nexus.git
cd zshooter-nexus
git submodule update --init --recursive

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

curl -fsSL https://d2lang.com/install.sh | sh -s --
python -m pip install -r requirements.txt

python -m unittest discover -s tests

python tools/stage_site.py

# Run these two commands only after changing D2 sources.
bash tools/render_d2.sh
bash tools/log_d2_drift.sh

# Always refresh the site copies and architecture viewer index.
bash tools/sync_d2_svgs.sh
python tools/generate_diagram_manifest.py

sphinx-build -b html -w docs/_build/sphinx-warnings.log docs docs/_build/html
python tools/validate_site.py \
  --html-root docs/_build/html \
  --warnings docs/_build/sphinx-warnings.log

python -m http.server -d docs/_build/html 8000
```
