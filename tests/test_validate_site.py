from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_site import REQUIRED_BOTH_MODE_PAGES, validate_modes


class SiteModeValidationTests(unittest.TestCase):
    def write_manifest(self, html_root: Path, manifest: dict[str, str]) -> None:
        payload = json.dumps(manifest, separators=(",", ":"))
        (html_root / "control.html").write_text(
            f"<script>window.__ZS_SITE_MODE_MANIFEST__ = {payload};</script>\n",
            encoding="utf-8",
        )

    def test_integrated_pages_are_visible_in_both_modes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            html_root = Path(directory)
            self.write_manifest(
                html_root,
                {page: "both" for page in REQUIRED_BOTH_MODE_PAGES},
            )

            self.assertEqual(validate_modes(html_root), [])

    def test_incorrect_visibility_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            html_root = Path(directory)
            manifest = {page: "both" for page in REQUIRED_BOTH_MODE_PAGES}
            manifest["_staged/drp/index.html"] = "internal"
            self.write_manifest(html_root, manifest)

            self.assertEqual(
                validate_modes(html_root),
                ["_staged/drp/index.html: expected mode 'both', found 'internal'"],
            )


if __name__ == "__main__":
    unittest.main()
