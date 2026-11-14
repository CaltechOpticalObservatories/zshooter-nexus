#!/usr/bin/env python3
"""Index rendered diagrams using the architecture package's human-readable catalog."""
from __future__ import annotations
import json
import re
from pathlib import Path


def natural_key(value: str) -> list:
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', value.lower())]


def title_from_stem(stem: str) -> str:
    return re.sub(r'\s+', ' ', stem.replace('_', ' ').replace('-', ' ')).strip() or stem


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog_path = root / 'zshooter-arch/diagrams.json'
    catalog = json.loads(catalog_path.read_text()) if catalog_path.exists() else {}
    svg_root = root / 'docs/_static/d2_diagrams'
    output = root / 'docs/_static/generated/diagrams.generated.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    paths = sorted(svg_root.glob('*.svg'), key=lambda p: (catalog.get(p.stem, {}).get('order', 1000), natural_key(p.stem)))
    entries = [{'title': catalog.get(p.stem, {}).get('title', title_from_stem(p.stem)),
                'file': f'd2_diagrams/{p.name}',
                'group': catalog.get(p.stem, {}).get('category', 'Target of Opportunity')}
               for p in paths]
    output.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
