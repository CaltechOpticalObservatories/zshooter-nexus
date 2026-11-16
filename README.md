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

## Source formats

Use Markdown for living design and team-edited content, and reStructuredText for stable site
structure and navigation. 

## Documentation ownership

| Owner | Canonical source | Generated nexus destination | Nexus landing page |
| --- | --- | --- | --- |
| ICS | `zshooter-ics/docs/source/` | `docs/_staged/ics/` | Technical Design → Controlling ZShooter |
| DRP | `zshooter-drp/docs/source/` and `zshooter-drp/notebooks/` | `docs/_staged/drp/` | Observing → Data Reduction |
| Simulator | `zshooter-sim/docs/`, `notebooks/`, `validation/` and `env/zshooter-stack.toml` | Matching paths under `docs/_staged/sim/` | Performance → Instrument Simulator |

The generated `_staged` tree is ignored by Git. Edit documentation only in its
canonical repository. Submodule revisions are deliberately pinned: update and
review a submodule gitlink in this repository when its documentation should be
published by the nexus.

The simulator landing page is `docs/simulator.rst`; topic navigation lives in
`docs/simulator/`. Its toctree entries are the publication list: add, rename or move
a notebook/report in its source repository, then update its navigation entry here.
Staging reports missing targets with their paths. Other simulator notebooks and
reports remain repository material, without becoming site pages or notebook downloads.
Links to those records go to GitHub. The running guide explains the development archive.
Staging retains figures and supporting data, and relocates Markdown links between
published files using their canonical source paths,
including links from simulator notebooks into DRP reports. Published pages, text
attachments and notebook downloads shorten recorded paths to repository or Python
environment paths. Canonical run records stay in their component repositories.
Notebook code, numbers, figures and execution counts are preserved; staging rejects
hard-coded personal paths in code cells so they can be fixed at the source. Download
copies retain their original relative document links. The site build never runs the
science calculations.

## Current assumptions

- CAD
  - `docs/cad.rst` embeds separate eDrawings and PDF viewers.
  - Both viewers discover files recursively from `https://meridian.caltech.edu/`; CAD assets are not
    mirrored in this
    repository.
  - `docs/cad_manifest.json` can place discovered files first and give them friendlier dropdown
    labels. Each entry has
    only `file` and `label`; blank labels and unlisted files display their filenames. The manifest
    is copied by Sphinx
    and has no generation step.
  - The CAD server must expose an HTML directory index and allow browser reads from the docs origin
    with
    `Access-Control-Allow-Origin`.
  - The wrappers support `cadRoot` overrides plus `selected`, `edrawing`, and `pdf` deep links.



## Development

Use Python 3.12 or later, Git and Pandoc (`brew install pandoc` on macOS).
Pandoc converts the stored notebook content for the site; notebook cells are not executed.
The D2 version below must match `.d2-version`.

```bash
git clone git@github.com:CaltechOpticalObservatories/zshooter-nexus.git
cd zshooter-nexus
git submodule update --init --recursive

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

curl -fsSL https://d2lang.com/install.sh | sh -s -- --method standalone --version "$(cat .d2-version)" --prefix "$HOME/.local"
export PATH="$HOME/.local/bin:$PATH"
python -m pip install -r requirements.txt

python -m unittest discover -s tests

python tools/stage_site.py

# Render only the architecture views during diagram work.
# Add --view zfront_connections to render one view. Omit --project to render both trees.
bash tools/render_d2.sh --project arch
python -m unittest discover -s zshooter-arch/tests
bash tools/log_d2_drift.sh

# Always refresh the site copies and architecture viewer index.
bash tools/sync_d2_svgs.sh
python tools/generate_diagram_manifest.py

sphinx-build -b html docs docs/_build/html

python -m http.server -d docs/_build/html 8000
```

D2 is pinned by `.d2-version`; local rendering checks that version. The architecture viewer supports
pan, zoom, enclosure focus and documentation links. Diagram source conventions are in
`zshooter-arch/README.md`. A compiler-pin or renderer change triggers regeneration in CI.

Commit diagram sources and their rendered SVGs in `zshooter-arch` together, then update its
submodule revision here. Publish the component commit before the parent change so other
checkouts and CI can retrieve it. Generated site copies and `_staged` content stay untracked.

Pull requests build the site for checking. After review, a push to `main` deploys it through
`.github/workflows/site.yml`. CAD publication is a separate Windows service; see the
[eDrawings Publisher repository](https://github.com/CaltechOpticalObservatories/eDrawingsPublisher).
