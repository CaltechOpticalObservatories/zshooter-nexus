# ZShooter prototype site configuration
import json
import os
import shutil
import sys
from collections import deque
from datetime import datetime
from pathlib import Path

from sphinx.util import logging

project = "ZShooter"
author = "Caltech Optical Observatories (COO)"
copyright = f"{datetime.now():%Y}, {author}"

logger = logging.getLogger(__name__)

VALID_ZS_MODES = {"both", "internal", "external"}
DEFAULT_ZS_MODE = "both"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "nbsphinx",
    "sphinx.ext.mathjax",
]


nbsphinx_execute = "never"
autosummary_generate = True
autodoc_typehints = "description"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "**/Thumbs.db",
    "**/.DS_Store",
]

html_theme = "shibuya"
html_static_path = ["_static"]
html_css_files = ["css/zshooter.css"]
html_js_files = ["js/site-mode.js"]

# html_sidebars = {
#     "_staged/sim/notebooks/**": [],
# }

html_title = "ZShooter"
html_logo = "_static/image/zshooter_sm.png"
html_favicon = "_static/image/zshooter_sm.png"

html_theme_options = {
    "accent_color": "blue",
}

myst_enable_extensions = ["colon_fence", "deflist", "linkify"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}


rst_prolog = """
.. role:: zs-check
   :class: zs-check
"""


ROOT = Path(__file__).resolve().parent.parent
CAD_SRC = ROOT / "cad"


def normalize_zs_mode(raw_value: str | None, *, docname: str | None = None) -> str | None:
    if raw_value is None:
        return None

    mode = str(raw_value).strip().lower()
    if not mode:
        return None

    if mode not in VALID_ZS_MODES:
        logger.warning(
            "Unsupported zs-mode %r in %s. Expected one of: %s.",
            raw_value,
            docname or "<unknown>",
            ", ".join(sorted(VALID_ZS_MODES)),
        )
        return None

    return mode


def build_zs_primary_parent_map(env, root_doc: str) -> dict[str, str]:
    parent_map: dict[str, str] = {}
    queue = deque([root_doc]) if root_doc in env.found_docs else deque()
    seen: set[str] = set()

    while queue:
        docname = queue.popleft()
        if docname in seen:
            continue
        seen.add(docname)

        for child in env.toctree_includes.get(docname, []):
            parent_map.setdefault(child, docname)
            if child not in seen:
                queue.append(child)

    return parent_map


def collect_zs_page_modes(app, env) -> None:
    explicit_modes = {
        docname: mode
        for docname in sorted(env.found_docs)
        if (mode := normalize_zs_mode(env.metadata.get(docname, {}).get("zs-mode"), docname=docname))
        is not None
    }
    parent_map = build_zs_primary_parent_map(env, app.config.root_doc)
    resolved_modes: dict[str, str] = {}

    def resolve(docname: str) -> str:
        if docname in resolved_modes:
            return resolved_modes[docname]

        explicit_mode = explicit_modes.get(docname)
        if explicit_mode is not None:
            resolved_modes[docname] = explicit_mode
            return explicit_mode

        parent = parent_map.get(docname)
        if parent is None:
            resolved_modes[docname] = DEFAULT_ZS_MODE
            return DEFAULT_ZS_MODE

        inherited_mode = resolve(parent)
        resolved_modes[docname] = inherited_mode if inherited_mode != DEFAULT_ZS_MODE else DEFAULT_ZS_MODE
        return resolved_modes[docname]

    for docname in sorted(env.found_docs):
        resolve(docname)

    env.zs_resolved_doc_modes = resolved_modes


def build_zs_mode_manifest(app) -> None:
    if hasattr(app, "_zs_mode_manifest_json"):
        return

    manifest: dict[str, str] = {}
    for docname, mode in sorted(getattr(app.env, "zs_resolved_doc_modes", {}).items()):
        try:
            target_uri = app.builder.get_target_uri(docname)
        except Exception:
            continue

        if target_uri:
            manifest[target_uri] = mode

    app._zs_mode_manifest_json = json.dumps(manifest, separators=(",", ":"), sort_keys=True)


def add_zs_page_context(app, pagename: str, templatename: str, context: dict, doctree) -> None:
    if app.builder.format != "html":
        return

    build_zs_mode_manifest(app)
    page_mode = getattr(app.env, "zs_resolved_doc_modes", {}).get(pagename, DEFAULT_ZS_MODE)
    context["zs_mode_manifest_json"] = getattr(app, "_zs_mode_manifest_json", "{}")
    context["zs_page_mode_json"] = json.dumps(page_mode)


def copy_local_cad_assets(app, exception) -> None:
    if exception is not None or app.builder.format != "html":
        return

    if not CAD_SRC.exists():
        return

    cad_dst = Path(app.outdir) / "cad"
    if cad_dst.exists():
        shutil.rmtree(cad_dst)
    shutil.copytree(CAD_SRC, cad_dst, ignore_dangling_symlinks=True)


def setup(app) -> dict[str, bool]:
    app.connect("env-updated", collect_zs_page_modes)
    app.connect("html-page-context", add_zs_page_context)
    app.connect("build-finished", copy_local_cad_assets)
    return {"parallel_read_safe": True}
