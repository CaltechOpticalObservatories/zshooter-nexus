# ZShooter prototype site configuration
import os
import sys
from datetime import datetime

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