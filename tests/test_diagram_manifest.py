from pathlib import Path
import importlib.util
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('diagram_manifest', Path(__file__).resolve().parents[1] / 'tools/generate_diagram_manifest.py')
manifest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manifest)


class DiagramManifest(unittest.TestCase):
    def test_title_comes_from_rendered_view(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'zshooter_ethernet.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><g class="dGl0bGU= title"><text>Ethernet Network(s)</text></g></svg>')
            self.assertEqual(manifest.title_from_svg(path), 'Ethernet Network(s)')

    def test_legacy_diagram_uses_filename_when_no_title_node(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'too_architecture.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
            self.assertEqual(manifest.title_from_svg(path), 'too architecture')
