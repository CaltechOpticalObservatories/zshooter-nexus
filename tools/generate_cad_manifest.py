#!/usr/bin/env python3
"""Generate lightweight CAD manifests for the ZShooter Sphinx site.

This script scans a sibling CAD tree and writes manifest JSON files consumed by
docs/_static/modelwrap.html and docs/_static/pdfwrap.html.

It is intentionally lightweight:
- no thumbnails required
- optional reuse of existing hand-maintained metadata files
- output is stable and sorted
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

MODEL_EXTS = {".step", ".stp", ".iges", ".igs", ".stl", ".obj", ".3mf", ".glb", ".gltf"}
DRAWING_EXTS = {".pdf"}
EDRAWING_EXTS = {".html", ".htm"}
REMOTE_CAD_ROOT = "http://zscad.astro.clatech.edu/"
REMOTE_LISTING_TIMEOUT_SECONDS = 10


def natural_key(value: str) -> List[object]:
    parts = re.split(r"(\d+)", value.lower())
    keyed: List[object] = []
    for part in parts:
        if part.isdigit():
            keyed.append(int(part))
        else:
            keyed.append(part)
    return keyed


def title_from_stem(stem: str) -> str:
    clean = stem.replace("_", " ").replace("-", " ").strip()
    clean = re.sub(r"\s+", " ", clean)
    return clean or stem


def read_optional_json(path: Path) -> List[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []


def build_metadata_index(items: Iterable[dict]) -> Dict[str, dict]:
    index: Dict[str, dict] = {}
    for item in items:
        file_value = str(item.get("file", "")).strip()
        title = item.get("title")
        docno = item.get("docno")
        notes = item.get("notes")
        payload = {k: v for k, v in {"title": title, "docno": docno, "notes": notes}.items() if v}

        if file_value:
            index[file_value] = payload
            index[Path(file_value).name] = payload
            index[Path(file_value).stem] = payload

        if title and title not in index:
            index[title] = payload
    return index


def find_files(root: Path, extensions: set[str]) -> List[Path]:
    if not root.exists():
        return []
    return [path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in extensions]


class DirectoryListingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: List[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.hrefs.append(value)


def read_remote_listing(url: str) -> List[str]:
    request = Request(url, headers={"User-Agent": "zshooter-cad-manifest/1.0"})
    with urlopen(request, timeout=REMOTE_LISTING_TIMEOUT_SECONDS) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        parser = DirectoryListingParser()
        parser.feed(response.read().decode(charset, errors="replace"))
    return parser.hrefs


def find_remote_files(remote_root: str, subdir: str, extensions: set[str]) -> List[str]:
    root_url = remote_root.rstrip("/") + "/"
    start_url = urljoin(root_url, subdir.strip("/") + "/")
    pending = [start_url]
    visited: set[str] = set()
    found: set[str] = set()

    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)

        try:
            hrefs = read_remote_listing(current)
        except Exception as exc:
            print(f"warning: could not read remote CAD listing {current}: {exc}", file=sys.stderr)
            continue

        for href in hrefs:
            clean_href = href.split("?", 1)[0].split("#", 1)[0]
            if not clean_href or clean_href in {"../", "./"}:
                continue

            candidate = urljoin(current, clean_href)
            if not candidate.startswith(root_url):
                continue

            parsed = urlparse(candidate)
            rel = parsed.path.removeprefix(urlparse(root_url).path).lstrip("/")
            if not rel:
                continue

            if clean_href.endswith("/"):
                pending.append(candidate)
                continue

            if Path(rel).suffix.lower() in extensions:
                found.add(rel)

    return sorted(found, key=natural_key)


def build_entries(
    paths: List[Path],
    base_dir: Path,
    web_root: str,
    metadata_index: Dict[str, dict],
    source: str,
) -> List[dict]:
    entries: List[dict] = []
    for path in paths:
        rel = path.relative_to(base_dir).as_posix()
        web_path = f"{web_root.rstrip('/')}/{rel}"
        metadata = (
            metadata_index.get(rel)
            or metadata_index.get(path.name)
            or metadata_index.get(path.stem)
            or {}
        )

        entry = {
            "title": metadata.get("title") or title_from_stem(path.stem),
            "file": web_path,
            "path": rel,
            "source": source,
        }

        if metadata.get("notes"):
            entry["notes"] = metadata["notes"]
        if metadata.get("docno"):
            entry["docno"] = metadata["docno"]

        entries.append(entry)

    entries.sort(key=lambda item: natural_key(item["title"]))
    return entries


def build_remote_entries(remote_paths: List[str], remote_root: str, metadata_index: Dict[str, dict]) -> List[dict]:
    entries: List[dict] = []
    base = remote_root.rstrip("/") + "/"
    for rel in remote_paths:
        path = Path(rel)
        metadata = metadata_index.get(rel) or metadata_index.get(path.name) or metadata_index.get(path.stem) or {}
        entry = {
            "title": metadata.get("title") or title_from_stem(path.stem),
            "file": urljoin(base, rel),
            "path": rel,
            "source": "remote",
        }
        if metadata.get("notes"):
            entry["notes"] = metadata["notes"]
        if metadata.get("docno"):
            entry["docno"] = metadata["docno"]
        entries.append(entry)

    entries.sort(key=lambda item: natural_key(item["title"]))
    return entries


def merge_entries(*entry_groups: List[dict]) -> List[dict]:
    merged: List[dict] = []
    seen_paths: set[str] = set()
    seen_files: set[str] = set()

    for group in entry_groups:
        for entry in group:
            rel = entry.get("path")
            file_value = entry.get("file")
            if rel and rel in seen_paths:
                continue
            if file_value in seen_files:
                continue
            if rel:
                seen_paths.add(rel)
            seen_files.add(file_value)
            merged.append(entry)

    merged.sort(key=lambda item: natural_key(item["title"]))
    return merged


def normalize_metadata_file_value(file_value: str) -> str:
    value = file_value.strip()
    if not value:
        return ""
    if value.startswith(("http://", "https://")):
        return value

    guessed = value
    while guessed.startswith("../"):
        guessed = guessed[3:]
    if guessed.startswith("cad/"):
        guessed = guessed[4:]
    return guessed.lstrip("/")


def seed_entries_from_metadata(items: List[dict], default_root: str, kind: str) -> List[dict]:
    entries: List[dict] = []
    source = "remote" if default_root.startswith(("http://", "https://")) else "local"

    for item in items:
        file_value = normalize_metadata_file_value(str(item.get("file", "")))
        if not file_value:
            continue

        if file_value.startswith(("http://", "https://")):
            file_path = file_value
            path_value = urlparse(file_value).path.lstrip("/")
            entry_source = "remote"
        else:
            file_path = f"{default_root.rstrip('/')}/{file_value}"
            path_value = file_value
            entry_source = source

        entry = {
            "title": item.get("title") or title_from_stem(Path(file_value).stem),
            "file": file_path,
            "path": path_value,
            "source": entry_source,
        }
        if item.get("notes"):
            entry["notes"] = item["notes"]
        if kind == "drawing" and item.get("docno"):
            entry["docno"] = item["docno"]
        entries.append(entry)

    entries.sort(key=lambda item: natural_key(item["title"]))
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cad-root", type=Path, required=True, help="Path to the source CAD tree, e.g. ../cad")
    parser.add_argument("--docs-root", type=Path, required=True, help="Path to the docs root, e.g. docs")
    parser.add_argument("--web-root", default="../cad", help="Public same-origin base URL for CAD assets")
    args = parser.parse_args()

    cad_root = args.cad_root.resolve()
    docs_root = args.docs_root.resolve()

    generated_dir = docs_root / "_static" / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    model_meta = build_metadata_index(read_optional_json(cad_root / "models.json"))
    drawing_meta = build_metadata_index(read_optional_json(cad_root / "drawings.json"))
    edrawing_meta = build_metadata_index(read_optional_json(cad_root / "edrawings.json"))

    model_paths = find_files(cad_root / "solids", MODEL_EXTS)
    drawing_paths = find_files(cad_root / "drawings", DRAWING_EXTS)
    edrawing_paths = find_files(cad_root / "solids", EDRAWING_EXTS)
    remote_model_paths = find_remote_files(REMOTE_CAD_ROOT, "solids", MODEL_EXTS)
    remote_drawing_paths = find_remote_files(REMOTE_CAD_ROOT, "drawings", DRAWING_EXTS)
    remote_edrawing_paths = find_remote_files(REMOTE_CAD_ROOT, "solids", EDRAWING_EXTS)

    local_model_entries = build_entries(model_paths, cad_root, args.web_root, model_meta, "local")
    local_drawing_entries = build_entries(drawing_paths, cad_root, args.web_root, drawing_meta, "local")
    local_edrawing_entries = build_entries(edrawing_paths, cad_root, args.web_root, edrawing_meta, "local")
    remote_model_entries = build_remote_entries(remote_model_paths, REMOTE_CAD_ROOT, model_meta)
    remote_drawing_entries = build_remote_entries(remote_drawing_paths, REMOTE_CAD_ROOT, drawing_meta)
    remote_edrawing_entries = build_remote_entries(remote_edrawing_paths, REMOTE_CAD_ROOT, edrawing_meta)

    model_entries = merge_entries(local_model_entries, remote_model_entries)
    drawing_entries = merge_entries(local_drawing_entries, remote_drawing_entries)
    edrawing_entries = merge_entries(local_edrawing_entries, remote_edrawing_entries)

    # If the real files are not present yet, seed from metadata so the page still has a useful scaffold.
    if not model_entries:
        model_entries = seed_entries_from_metadata(
            read_optional_json(cad_root / "models.json"),
            REMOTE_CAD_ROOT or args.web_root,
            "model",
        )

    if not drawing_entries:
        drawing_entries = seed_entries_from_metadata(
            read_optional_json(cad_root / "drawings.json"),
            REMOTE_CAD_ROOT or args.web_root,
            "drawing",
        )

    if not edrawing_entries:
        edrawing_entries = seed_entries_from_metadata(
            read_optional_json(cad_root / "edrawings.json"),
            REMOTE_CAD_ROOT or args.web_root,
            "model",
        )

    (generated_dir / "models.generated.json").write_text(json.dumps(model_entries, indent=2) + "\n", encoding="utf-8")
    (generated_dir / "drawings.generated.json").write_text(json.dumps(drawing_entries, indent=2) + "\n", encoding="utf-8")
    (generated_dir / "edrawings.generated.json").write_text(json.dumps(edrawing_entries, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
