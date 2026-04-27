#!/usr/bin/env python3
"""Generate a manifest for rendered D2 SVG artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path


def natural_key(value: str) -> list[object]:
    parts = re.split(r"(\d+)", value.lower())
    keyed: list[object] = []
    for part in parts:
        keyed.append(int(part) if part.isdigit() else part)
    return keyed


def title_from_stem(stem: str) -> str:
    clean = stem.replace("_", " ").replace("-", " ").strip()
    clean = re.sub(r"\s+", " ", clean)
    return clean or stem


def main() -> None:
    docs_root = Path("docs")
    svg_root = docs_root / "_static" / "d2_diagrams"
    generated_root = docs_root / "_static" / "generated"
    generated_root.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, str]] = []
    for path in sorted(svg_root.glob("*.svg"), key=lambda p: natural_key(p.stem)):
        entries.append(
            {
                "title": title_from_stem(path.stem),
                "file": f"d2_diagrams/{path.name}",
            }
        )

    output_path = generated_root / "diagrams.generated.json"
    output_path.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
