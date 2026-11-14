#!/usr/bin/env python3
"""Render selected views with the reviewed D2 version; publish each SVG atomically."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def render(root: Path, project: str, views: list[str], binary: str) -> list[dict]:
    required = (root / '.d2-version').read_text().strip().removeprefix('v')
    actual = subprocess.check_output([binary, '--version'], text=True).strip().removeprefix('v')
    if actual != required:
        raise RuntimeError(f'D2 {required} is required; found {actual}. See README.md.')
    trees = ['zshooter-arch', 'zshooter-too'] if project == 'all' else ['zshooter-' + project]
    selected = []
    for tree in trees:
        folder = root / tree
        catalog = json.loads((folder / 'diagrams.json').read_text()) if (folder / 'diagrams.json').exists() else {}
        for path in sorted((folder / 'views').glob('*.d2')):
            if not views or path.stem in views:
                selected.append((tree, path, catalog.get(path.stem, {})))
    missing = set(views) - {p.stem for _, p, _ in selected}
    if missing or not selected:
        raise RuntimeError('No matching view: ' + ', '.join(sorted(missing or set(views))))
    results = []
    for tree, path, config in selected:
        destination = root / tree / 'svg' / (path.stem + '.svg')
        destination.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix='.' + path.stem + '-', suffix='.svg', dir=destination.parent)
        os.close(fd)
        start = time.monotonic()
        try:
            cmd = [binary, '--layout', config.get('layout', 'elk'), '--timeout', '120']
            if tree == 'zshooter-arch':
                cmd += ['--elk-nodeNodeBetweenLayers', '25', '--elk-edgeNodeBetweenLayers', '15']
            subprocess.run(cmd + [str(path), temporary], check=True, timeout=130)
            if ET.parse(temporary).getroot().tag != "{http://www.w3.org/2000/svg}svg":
                raise RuntimeError(f"D2 did not produce SVG for {path.name}")
            Path(temporary).replace(destination)
        finally:
            Path(temporary).unlink(missing_ok=True)
        elapsed = round(time.monotonic() - start, 3)
        results.append({'project': tree, 'view': path.stem, 'seconds': elapsed, 'd2': required})
        print(f'{tree}/{path.stem}: {elapsed:.3f}s', flush=True)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', choices=['arch', 'too', 'all'], default='all')
    parser.add_argument('--view', action='append', default=[], help='View stem; repeat to select several')
    parser.add_argument('--timings', type=Path, help='Optional JSON timing record')
    args = parser.parse_args()
    results = render(ROOT, args.project, args.view, os.environ.get('D2_BIN', 'd2'))
    if args.timings:
        args.timings.parent.mkdir(parents=True, exist_ok=True)
        args.timings.write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
