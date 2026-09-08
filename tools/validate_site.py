#!/usr/bin/env python3
"""Validate the generated pages and warning boundary for integrated docs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_PAGES = (
    "control.html",
    "_staged/ics/index.html",
    "_staged/ics/architecture/index.html",
    "reduction.html",
    "_staged/drp/index.html",
    "_staged/drp/getting-started.html",
    "_staged/drp/notebooks/extraction_demo.html",
    "simulator.html",
    "_staged/sim/notebooks/What_does_scopesim_do.html",
)

REQUIRED_BOTH_MODE_PAGES = (
    "control.html",
    "_staged/ics/index.html",
    "_staged/ics/architecture/index.html",
    "reduction.html",
    "_staged/drp/index.html",
    "_staged/drp/getting-started.html",
    "_staged/drp/notebooks/extraction_demo.html",
)

MODE_MANIFEST_PATTERN = re.compile(
    r"window\.__ZS_SITE_MODE_MANIFEST__\s*=\s*(\{.*?\});",
    re.DOTALL,
)

MONITORED_WARNING_PATHS = (
    "/docs/_staged/ics/",
    "/docs/_staged/drp/",
    "/docs/control.rst",
    "/docs/reduction.rst",
    "/docs/technical.rst",
    "/docs/observing.rst",
)


def validate_pages(html_root: Path) -> list[str]:
    return [page for page in REQUIRED_PAGES if not (html_root / page).is_file()]


def validate_modes(html_root: Path) -> list[str]:
    manifest_page = html_root / "control.html"
    if not manifest_page.is_file():
        return []

    match = MODE_MANIFEST_PATTERN.search(manifest_page.read_text(encoding="utf-8"))
    if match is None:
        return [f"Site-mode manifest is missing from {manifest_page}"]

    try:
        manifest = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        return [f"Site-mode manifest is invalid JSON: {error}"]

    return [
        f"{page}: expected mode 'both', found {manifest.get(page)!r}"
        for page in REQUIRED_BOTH_MODE_PAGES
        if manifest.get(page) != "both"
    ]


def monitored_warnings(warnings_file: Path) -> list[str]:
    if not warnings_file.is_file():
        return [f"Sphinx warnings file is missing: {warnings_file}"]

    failures: list[str] = []
    for line in warnings_file.read_text(encoding="utf-8").splitlines():
        normalized = line.replace("\\", "/")
        if not any(fragment in normalized for fragment in MONITORED_WARNING_PATHS):
            continue

        # The canonical extraction notebook intentionally retains legacy
        # lexer metadata. Its standalone DRP build suppresses this exact
        # warning; the nexus accepts only that same narrow exception.
        if (
            "/docs/_staged/drp/notebooks/" in normalized
            and "[misc.highlighting_failure]" in normalized
        ):
            continue
        failures.append(line)
    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-root", type=Path, required=True)
    parser.add_argument("--warnings", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    missing_pages = validate_pages(args.html_root)
    mode_failures = validate_modes(args.html_root)
    warning_failures = monitored_warnings(args.warnings)

    if missing_pages:
        print("Missing required site pages:")
        for page in missing_pages:
            print(f"  - {page}")
    if warning_failures:
        print("Warnings from integrated documentation:")
        for warning in warning_failures:
            print(f"  - {warning}")
    if mode_failures:
        print("Integrated documentation with incorrect site visibility:")
        for failure in mode_failures:
            print(f"  - {failure}")
    if missing_pages or mode_failures or warning_failures:
        raise SystemExit(1)

    print(
        f"Validated {len(REQUIRED_PAGES)} required site pages, "
        f"{len(REQUIRED_BOTH_MODE_PAGES)} visibility rules, and integrated-doc warnings."
    )


if __name__ == "__main__":
    main()
