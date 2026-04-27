# ZShooter prototype site configuration
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

project = "ZShooter"
author = "Caltech Optical Observatories (COO)"
copyright = f"{datetime.now():%Y}, {author}"

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
    app.connect("build-finished", copy_local_cad_assets)
    return {"parallel_read_safe": True}
