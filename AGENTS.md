# AGENTS.md

## Docs Build

Build the site with:

```bash
sphinx-build -b html docs docs/_build/html
```

The local `make` file is a shell-style script, not a Makefile. It stages generated content, builds docs, and then starts a web server.

## CAD Page Debugging

The technical drawings page is `docs/cad.rst`. It embeds wrappers from `docs/_static/`:

- `edrawingswrap.html`
- `pdfwrap.html`

Both wrappers discover files recursively from the HTML directory listing at `https://meridian.caltech.edu/`. 

`docs/cad_manifest.json` is a hand-maintained, optional ordering and label overlay for files found in that listing.
Each entry contains only `file` and `label`. The manifest does not replace directory discovery and must not gain a
generator or workflow step; Sphinx publishes it through `html_extra_path`.

CAD listings and files are fetched client-side, so browser security policy matters.

Do not infer the root cause from `TypeError: Failed to fetch` alone. Use browser developer tooling, or Chrome DevTools Protocol, to inspect `Network.loadingFailed`, `blockedReason`, and `corsErrorStatus`.

Useful probe:

```bash
curl -i -H 'Origin: https://zshooter.astro.caltech.edu' https://meridian.caltech.edu/
```

## Git Hygiene

The worktree may contain unrelated generated documentation or dependency lockfile changes. Do not revert unrelated user changes.
