"""Failure must not replace the last usable render or alter unrelated views."""
import base64
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

SPEC = importlib.util.spec_from_file_location('render_d2', Path(__file__).resolve().parents[1] / 'tools/render_d2.py')
RENDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDER)


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / '.d2-version').write_text('0.9.0\n')
        self.views = self.root / 'zshooter-arch/views'; self.views.mkdir(parents=True)
        self.svgs = self.root / 'zshooter-arch/svg'; self.svgs.mkdir()
        for name in ['first', 'second']:
            (self.views / f'{name}.d2').write_text('a -> b\n')
            (self.svgs / f'{name}.svg').write_text('previous ' + name)
        self.binary = self.root / 'fake-d2'

    def program(self, content):
        self.binary.write_text('#!/bin/sh\nif [ "$1" = "--version" ]; then echo v0.9.0; exit 0; fi\n' + content)
        self.binary.chmod(0o755)

    def test_failed_render_preserves_previous_svg(self):
        self.program('exit 1\n')
        with self.assertRaises(subprocess.CalledProcessError):
            RENDER.render(self.root, 'arch', ['first'], str(self.binary))
        self.assertEqual((self.svgs / 'first.svg').read_text(), 'previous first')
        self.assertEqual(sorted(p.name for p in self.svgs.iterdir()), ['first.svg', 'second.svg'])

    def test_invalid_svg_preserves_previous_render(self):
        self.program('for arg do destination="$arg"; done\nprintf broken > "$destination"\n')
        with self.assertRaises(ET.ParseError):
            RENDER.render(self.root, 'arch', ['first'], str(self.binary))
        self.assertEqual((self.svgs / 'first.svg').read_text(), 'previous first')

    def test_selected_view_does_not_touch_other_views(self):
        self.program('for arg do destination="$arg"; done\nprintf \'<svg xmlns="http://www.w3.org/2000/svg"/>\' > "$destination"\n')
        result = RENDER.render(self.root, 'arch', ['first'], str(self.binary))
        self.assertEqual([row['view'] for row in result], ['first'])
        self.assertEqual((self.svgs / 'second.svg').read_text(), 'previous second')
        self.assertTrue((self.svgs / 'first.svg').read_text().startswith('<svg'))

    def test_wrong_version_fails_before_render(self):
        self.binary.write_text('#!/bin/sh\necho v0.8.2\n'); self.binary.chmod(0o755)
        with self.assertRaisesRegex(RuntimeError, '0.9.0 is required'):
            RENDER.render(self.root, 'arch', [], str(self.binary))
        self.assertEqual((self.svgs / 'first.svg').read_text(), 'previous first')


class LinkTargets(unittest.TestCase):
    def test_container_labels_keep_links_and_background_tooltips(self):
        # Match the flat object groups and separate link icon emitted by D2 0.9.
        ns = RENDER.NS
        key = lambda value: base64.b64encode(value.encode()).decode()
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'diagram.svg'
            output.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg">
              <a href="assembly.html"><g class="{key('assembly')} module">
                <title>Background context</title><g class="shape"><rect width="400" height="300"/></g>
                <text>Assembly</text>
              </g></a>
              <a href="device.html"><g class="{key('assembly.device')} device">
                <title>Device context</title><g class="shape"><rect width="100" height="60"/></g>
                <text>Device</text>
              </g></a>
              <a href="assembly.html" class="link-icon"><path d="M0,0 L10,10"/></a>
              <g><rect width="200" height="200"/><text>Legend</text><text>DC</text></g>
            </svg>''')
            RENDER.prepare_arch_svg(output)
            root = ET.parse(output).getroot()
            parents = {child: parent for parent in root.iter() for child in parent}
            groups = {RENDER.object_key(g): g for g in root.iter(ns + 'g')}
            container, device = groups['assembly'], groups['assembly.device']
            self.assertIs(parents[container], root)
            self.assertEqual(container.find(ns + 'title').text, 'Background context')
            self.assertIsNotNone(container.find(ns + 'g/' + ns + 'rect'))
            label = container.find(ns + 'a/' + ns + 'text')
            self.assertEqual(label.text, 'Assembly')
            self.assertEqual(parents[label].get('href'), 'assembly.html')
            self.assertEqual(parents[device].get('href'), 'device.html')
            self.assertIsNotNone(root.find(ns + 'a[@class="link-icon"]/' + ns + 'path'))
            legend = next(t for t in root.iter(ns + 'text') if t.text == 'Legend')
            self.assertEqual(parents[legend].get('href'), RENDER.GUIDE)
            self.assertEqual(root.find('.//' + ns + 'rect[@data-d2-legend]').get('data-d2-legend'), 'true')
            # Reprocessing a committed SVG must not create nested anchors or drift.
            first = output.read_bytes()
            RENDER.prepare_arch_svg(output)
            self.assertEqual(output.read_bytes(), first)


if __name__ == '__main__':
    unittest.main()
