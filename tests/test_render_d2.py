"""Failure must not replace the last usable render or alter unrelated views."""
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


if __name__ == '__main__':
    unittest.main()
