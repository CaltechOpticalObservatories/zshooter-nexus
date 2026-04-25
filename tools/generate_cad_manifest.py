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
from pathlib import Path
from typing import Dict, Iterable, List

MODEL_EXTS = {".step", ".stp", ".iges", ".igs", ".stl", ".obj", ".3mf", ".glb", ".gltf"}
DRAWING_EXTS = {".pdf"}


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


def build_entries(paths: List[Path], base_dir: Path, web_root: str, metadata_index: Dict[str, dict]) -> List[dict]:
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
        }

        if metadata.get("notes"):
            entry["notes"] = metadata["notes"]
        if metadata.get("docno"):
            entry["docno"] = metadata["docno"]

        entries.append(entry)

    entries.sort(key=lambda item: natural_key(item["title"]))
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cad-root", type=Path, required=True, help="Path to the source CAD tree, e.g. ../cad")
    parser.add_argument("--docs-root", type=Path, required=True, help="Path to the docs root, e.g. docs")
    parser.add_argument("--web-root", default="/cad", help="Public same-origin base URL for CAD assets")
    args = parser.parse_args()

    cad_root = args.cad_root.resolve()
    docs_root = args.docs_root.resolve()

    generated_dir = docs_root / "_static" / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    model_meta = build_metadata_index(read_optional_json(cad_root / "models.json"))
    drawing_meta = build_metadata_index(read_optional_json(cad_root / "drawings.json"))

    model_paths = find_files(cad_root / "solids", MODEL_EXTS)
    drawing_paths = find_files(cad_root / "drawings", DRAWING_EXTS)

    model_entries = build_entries(model_paths, cad_root, args.web_root, model_meta)
    drawing_entries = build_entries(drawing_paths, cad_root, args.web_root, drawing_meta)

    # If the real files are not present yet, seed from metadata so the page still has a useful scaffold.
    if not model_entries:
        for item in read_optional_json(cad_root / "models.json"):
            file_value = str(item.get("file", "")).strip()
            if not file_value:
                continue
            guessed = file_value.replace("../", "").replace("cad/", "")
            file_path = f"{args.web_root.rstrip('/')}/{guessed.lstrip('/')}"
            entry = {"title": item.get("title") or title_from_stem(Path(file_value).stem), "file": file_path}
            if item.get("notes"):
                entry["notes"] = item["notes"]
            model_entries.append(entry)
        model_entries.sort(key=lambda item: natural_key(item["title"]))

    if not drawing_entries:
        for item in read_optional_json(cad_root / "drawings.json"):
            file_value = str(item.get("file", "")).strip()
            if not file_value:
                continue
            guessed = file_value.replace("../", "").replace("cad/", "")
            file_path = f"{args.web_root.rstrip('/')}/{guessed.lstrip('/')}"
            entry = {"title": item.get("title") or title_from_stem(Path(file_value).stem), "file": file_path}
            if item.get("docno"):
                entry["docno"] = item["docno"]
            if item.get("notes"):
                entry["notes"] = item["notes"]
            drawing_entries.append(entry)
        drawing_entries.sort(key=lambda item: natural_key(item["title"]))

    (generated_dir / "models.generated.json").write_text(json.dumps(model_entries, indent=2) + "\n", encoding="utf-8")
    (generated_dir / "drawings.generated.json").write_text(json.dumps(drawing_entries, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
