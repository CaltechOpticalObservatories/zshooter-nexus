#!/usr/bin/env python3
"""Compose documentation owned by ZShooter subprojects into one Sphinx tree."""

from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
STAGED = DOCS / "_staged"

IGNORED_NAMES = {
    ".DS_Store",
    ".ipynb_checkpoints",
    "__pycache__",
    "*.pyc",
    ".gitignore",
}


@dataclass(frozen=True)
class StageSpec:
    """One generated subtree inside ``docs/_staged``."""

    name: str
    destination: Path
    docs_source: Path | None = None
    notebooks_source: Path | None = None
    excluded_source_names: frozenset[str] = field(default_factory=frozenset)
    require_index: bool = True
    docs_subdir: Path = Path(".")
    additional_sources: tuple[tuple[Path, Path], ...] = ()

    def sources(self) -> tuple[tuple[Path, Path], ...]:
        """Canonical paths and their locations relative to this staged tree."""
        paths = list(self.additional_sources)
        if self.docs_source is not None:
            paths.append((self.docs_source, self.docs_subdir))
        if self.notebooks_source is not None:
            paths.append((self.notebooks_source, Path("notebooks")))
        return tuple(paths)


STAGE_SPECS = (
    StageSpec(
        name="ICS",
        docs_source=ROOT / "zshooter-ics" / "docs" / "source",
        destination=STAGED / "ics",
        excluded_source_names=frozenset({"conf.py", "_templates", "requirements"}),
    ),
    StageSpec(
        name="DRP",
        docs_source=ROOT / "zshooter-drp" / "docs" / "source",
        notebooks_source=ROOT / "zshooter-drp" / "notebooks",
        destination=STAGED / "drp",
        # The DRP's standalone build may already contain its ignored notebook
        # staging directory. Always use the canonical top-level notebooks.
        excluded_source_names=frozenset({"conf.py", "_templates", "notebooks"}),
    ),
    StageSpec(
        name="simulator",
        docs_source=ROOT / "zshooter-sim" / "docs",
        docs_subdir=Path("docs"),
        notebooks_source=ROOT / "zshooter-sim" / "notebooks",
        destination=STAGED / "sim",
        excluded_source_names=frozenset({"conf.py", "_templates"}),
        additional_sources=(
            (ROOT / "zshooter-sim" / "validation", Path("validation")),
            (ROOT / "zshooter-sim" / "env" / "zshooter-stack.toml", Path("env/zshooter-stack.toml")),
        ),
    ),
)


def _ignore_names(extra_names: frozenset[str] = frozenset()):
    patterns = sorted(IGNORED_NAMES | set(extra_names))
    return shutil.ignore_patterns(*patterns)


def _validate_directory(path: Path, label: str) -> None:
    if not path.is_dir():
        raise FileNotFoundError(f"Missing {label} directory: {path}")


def _has_index(path: Path) -> bool:
    return any((path / filename).is_file() for filename in ("index.rst", "index.md"))


def stage_project(spec: StageSpec) -> int:
    """Build one staged subtree atomically and return its file count."""
    temporary = spec.destination.with_name(f".{spec.destination.name}.staging")
    if temporary.exists():
        shutil.rmtree(temporary)

    temporary.parent.mkdir(parents=True, exist_ok=True)
    temporary.mkdir()

    try:
        if spec.docs_source is not None:
            _validate_directory(spec.docs_source, f"{spec.name} documentation source")
            shutil.copytree(
                spec.docs_source,
                temporary / spec.docs_subdir,
                dirs_exist_ok=True,
                ignore=_ignore_names(spec.excluded_source_names),
            )

        if spec.notebooks_source is not None:
            _validate_directory(spec.notebooks_source, f"{spec.name} notebook source")
            shutil.copytree(
                spec.notebooks_source,
                temporary / "notebooks",
                dirs_exist_ok=True,
                ignore=_ignore_names(),
            )

        for source, relative_destination in spec.additional_sources:
            destination = temporary / relative_destination
            if source.is_dir():
                shutil.copytree(source, destination, ignore=_ignore_names())
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)

        if spec.require_index and not _has_index(temporary / spec.docs_subdir):
            raise FileNotFoundError(
                f"{spec.name} documentation has no index.rst or index.md in {spec.docs_source}"
            )

        prepare_publication(temporary)
        if spec.destination.exists():
            shutil.rmtree(spec.destination)
        temporary.replace(spec.destination)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise

    return sum(1 for path in spec.destination.rglob("*") if path.is_file())


HOME_PREFIX = r"/(?:Users|home)/[^/\s\"'<>]+"
PATH_COMPONENT = r"[^/\s\"'<>\x1b]+"
ENVIRONMENT_PREFIX = re.compile(
    HOME_PREFIX + r"/(?:" + PATH_COMPONENT + r"/)*?"
    r"(?:\.venv|(?:miniforge\d*|mambaforge|miniconda\d*|anaconda\d*)/envs/" + PATH_COMPONENT + r")(?=/)"
)
REPOSITORY_PREFIX = re.compile(
    HOME_PREFIX + r"/(?:" + PATH_COMPONENT + r"/)*?"
    r"(?P<repository>zs-scopesim|zshooter-sim|zshooter-drp|irdb|[Ss]cope[Ss]im|PyReduce(?:-[^/\s\"'<>]+)?)"
    r"(?=/|[\s\"'<>]|$)"
)
PERSONAL_PATH = re.compile(HOME_PREFIX + r"|[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]")
TEXT_ASSETS = {".md", ".rst", ".txt", ".csv", ".ecsv", ".diff", ".py", ".toml", ".json", ".html", ".svg"}


def portable_paths(text: str) -> str:
    """Shorten recorded checkout/environment paths without changing their tails."""
    text = ENVIRONMENT_PREFIX.sub("python-environment", text)
    text = REPOSITORY_PREFIX.sub(lambda match: match["repository"], text)
    return re.sub(HOME_PREFIX, "~", text)


def portable_notebook_value(value):
    if isinstance(value, str):
        return portable_paths(value)
    if isinstance(value, list):
        return [portable_notebook_value(item) for item in value]
    if isinstance(value, dict):
        # Keep image representations byte-for-byte; only text is being edited.
        return {
            key: item if key.startswith("image/") or key == "application/pdf" else portable_notebook_value(item)
            for key, item in value.items()
        }
    return value


def prepare_publication(directory: Path) -> None:
    """Prepare portable site copies while leaving canonical run records intact.

    Download copies retain the notebooks' original relative Markdown links.
    Relocation for the combined website happens separately, after this step.
    """
    for path in list(directory.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_ASSETS | {".ipynb"}:
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix == ".ipynb":
            notebook = json.loads(text)
            for number, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] == "code" and PERSONAL_PATH.search("".join(cell["source"])):
                    raise ValueError(f"Use a portable path in {path}, code cell {number}; publication does not rewrite executable code")
            notebook = portable_notebook_value(notebook)
            updated = json.dumps(notebook, ensure_ascii=False, indent=1) + "\n"
        else:
            updated = portable_paths(text)
        if PERSONAL_PATH.search(updated):
            raise ValueError(f"Unresolved personal path in publication copy: {path}")
        if updated != text:
            path.write_text(updated, encoding="utf-8")
        if path.suffix == ".ipynb":
            download = directory / "_downloads" / path.relative_to(directory)
            download.parent.mkdir(parents=True, exist_ok=True)
            download.write_text(updated, encoding="utf-8")


MARKDOWN_LINK = re.compile(
    r"(?P<inline>\]\(\s*<?)(?P<url>[^\s<>)]+)"
    r"|(?P<reference>^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*<?)(?P<refurl>[^\s<>]+)",
    re.MULTILINE,
)
INLINE_CODE = re.compile(r"(`+).*?\1")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")


def rewrite_markdown_links(text: str, rewrite_url) -> str:
    """Relocate Markdown links, leaving code examples and their URLs alone."""
    fences = []
    lines = []
    for line in text.splitlines(keepends=True):
        opening = FENCE.match(line)
        if opening and fences and opening[1].startswith(fences[-1][0]) and not opening[2].strip():
            fences.pop()
            lines.append(line)
            continue
        if fences and fences[-1][1]:
            lines.append(line)
            continue
        if opening:
            is_code = not opening[2].lstrip().startswith("{") or opening[2].lstrip().startswith("{code-block}")
            fences.append((opening[1], is_code))
            lines.append(line)
            continue

        def replace(match):
            prefix = match["inline"] or match["reference"]
            return prefix + rewrite_url(match["url"] or match["refurl"])

        # Inline code can contain example Markdown links, so protect those spans.
        start = 0
        parts = []
        for code in INLINE_CODE.finditer(line):
            parts.append(MARKDOWN_LINK.sub(replace, line[start:code.start()]))
            parts.append(code[0])
            start = code.end()
        parts.append(MARKDOWN_LINK.sub(replace, line[start:]))
        lines.append("".join(parts))
    return "".join(lines)


def relocate_links(specs: tuple[StageSpec, ...]) -> None:
    """Resolve links by canonical source location, including across subprojects.

    Only the generated copies change. Notebook code, outputs and metadata retain
    their stored values; Markdown cells get the same URL mapping as report pages.
    """
    published = {}
    for spec in specs:
        for source, relative in spec.sources():
            destination = spec.destination / relative
            published[source.resolve()] = destination
            if destination.is_dir():
                for path in destination.rglob("*"):
                    relative = path.relative_to(destination)
                    if source == spec.docs_source and any(part in spec.excluded_source_names for part in relative.parts):
                        continue
                    original = source / relative
                    if original.exists():
                        published[original.resolve()] = path

    for source, destination in list(published.items()):
        if not destination.is_file() or destination.suffix not in {".md", ".ipynb"}:
            continue

        def rewrite_url(url: str) -> str:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
                return url
            original = (source.parent / unquote(parts.path)).resolve()
            target = published.get(original)
            if target is None or target.is_dir():
                return url
            relative = Path(os.path.relpath(target, destination.parent)).as_posix()
            return urlunsplit(("", "", quote(relative, safe="/"), parts.query, parts.fragment))

        original_text = destination.read_text(encoding="utf-8")
        if destination.suffix == ".md":
            updated_text = rewrite_markdown_links(original_text, rewrite_url)
        else:
            notebook = json.loads(original_text)
            changed = False
            for cell in notebook["cells"]:
                if cell["cell_type"] != "markdown":
                    continue
                source_text = cell["source"]
                text = "".join(source_text)
                updated = rewrite_markdown_links(text, rewrite_url)
                if updated != text:
                    cell["source"] = updated.splitlines(keepends=True) if isinstance(source_text, list) else updated
                    changed = True
            updated_text = json.dumps(notebook, ensure_ascii=False, indent=1) + "\n" if changed else original_text
        if updated_text != original_text:
            destination.write_text(updated_text, encoding="utf-8")


def main() -> None:
    STAGED.mkdir(parents=True, exist_ok=True)
    summaries = [f"{spec.name}: {stage_project(spec)} files" for spec in STAGE_SPECS]
    relocate_links(STAGE_SPECS)
    print("Staged subproject documentation (" + ", ".join(summaries) + ")")


if __name__ == "__main__":
    main()
