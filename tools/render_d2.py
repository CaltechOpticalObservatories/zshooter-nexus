#!/usr/bin/env python3
"""Render selected views with the reviewed D2 version; publish each SVG atomically."""
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


NS = '{http://www.w3.org/2000/svg}'
XLINK = '{http://www.w3.org/1999/xlink}'
GUIDE = '../../controls/harnesses/diagram-guide.html'


def object_key(group):
    """D2 0.9 places the encoded object path in the first SVG class."""
    if group.tag != NS + 'g':
        return None
    classes = group.get('class', '').split()
    if not classes:
        return None
    try:
        key = base64.b64decode(classes[0], validate=True).decode()
    except (ValueError, UnicodeDecodeError):
        return None
    return key if '(' not in key else None


def prepare_arch_svg(path: Path):
    """Change click targets, preserving geometry, device links and native titles."""
    ET.register_namespace('', NS[1:-1])
    ET.register_namespace('xlink', XLINK[1:-1])
    tree = ET.parse(path)
    root = tree.getroot()
    keys = {key for group in root.iter(NS + 'g') if (key := object_key(group))}
    containers = set()
    for key in keys:
        while '.' in key:
            key = key.rsplit('.', 1)[0]
            containers.add(key)
    parents = {child: parent for parent in root.iter() for child in parent}
    for anchor in list(root.iter(NS + 'a')):
        children = list(anchor)
        if len(children) != 1:
            continue
        group = children[0]
        if object_key(group) not in containers:
            continue
        parent = parents[anchor]
        index = list(parent).index(anchor)
        anchor.remove(group)
        parent.remove(anchor)
        parent.insert(index, group)
        # Keep the title on the group: background hover still shows its tooltip.
        # Leaf devices and D2's separate link/information icons are untouched.
        for label in list(group):
            if label.tag != NS + 'text':
                continue
            index = list(group).index(label)
            link = ET.Element(NS + 'a', {**anchor.attrib, 'class': 'container-label-link'})
            group.remove(label)
            link.append(label)
            group.insert(index, link)

    parents = {child: parent for parent in root.iter() for child in parent}
    for title in list(root.iter(NS + 'text')):
        if ''.join(title.itertext()) != 'Legend':
            continue
        parent = parents[title]
        if parent.tag == NS + 'a':
            continue
        index = list(parent).index(title)
        if index and parent[index - 1].tag == NS + 'rect':
            parent[index - 1].set('data-d2-legend', 'true')
        link = ET.Element(NS + 'a', {'href': GUIDE, XLINK + 'href': GUIDE})
        ET.SubElement(link, NS + 'title').text = 'Reading the architecture diagrams'
        title.set('text-decoration', 'underline')
        parent.remove(title)
        link.append(title)
        parent.insert(index, link)
    tree.write(path, encoding='unicode')


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
            if tree == 'zshooter-arch':
                prepare_arch_svg(Path(temporary))
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
