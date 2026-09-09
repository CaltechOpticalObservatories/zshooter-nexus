#!/usr/bin/env python3
"""Compose documentation owned by ZShooter subprojects into one Sphinx tree."""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
STAGED = DOCS / "_staged"

IGNORED_NAMES = {
    ".DS_Store",
    ".ipynb_checkpoints",
    "__pycache__",
    "*.pyc",
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
        notebooks_source=ROOT / "zshooter-sim" / "notebooks",
        destination=STAGED / "sim",
        require_index=False,
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
                temporary,
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

        if spec.require_index and not _has_index(temporary):
            raise FileNotFoundError(
                f"{spec.name} documentation has no index.rst or index.md in {spec.docs_source}"
            )

        if spec.destination.exists():
            shutil.rmtree(spec.destination)
        temporary.replace(spec.destination)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise

    return sum(1 for path in spec.destination.rglob("*") if path.is_file())


def main() -> None:
    STAGED.mkdir(parents=True, exist_ok=True)
    summaries = [f"{spec.name}: {stage_project(spec)} files" for spec in STAGE_SPECS]
    print("Staged subproject documentation (" + ", ".join(summaries) + ")")


if __name__ == "__main__":
    main()
