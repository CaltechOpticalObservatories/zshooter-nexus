from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.stage_site import StageSpec, stage_project


class StageProjectTests(unittest.TestCase):
    def test_recursive_sources_notebooks_exclusions_and_stale_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            notebooks = root / "notebooks"
            destination = root / "staged" / "project"

            (source / "guide").mkdir(parents=True)
            (source / "_static").mkdir()
            (source / "_templates").mkdir()
            (source / "requirements").mkdir()
            notebooks.mkdir()

            (source / "index.md").write_text("# Index\n", encoding="utf-8")
            (source / "guide" / "page.rst").write_text("Page\n====\n", encoding="utf-8")
            (source / "_static" / "figure.svg").write_text("<svg/>\n", encoding="utf-8")
            (source / "conf.py").write_text("project = 'child'\n", encoding="utf-8")
            (source / "_templates" / "layout.html").write_text("child\n", encoding="utf-8")
            (source / "requirements" / "draft.rst").write_text("Draft\n=====\n", encoding="utf-8")
            (notebooks / "README.md").write_text("Notebook assets\n", encoding="utf-8")

            destination.mkdir(parents=True)
            (destination / "stale.txt").write_text("stale\n", encoding="utf-8")

            stage_project(
                StageSpec(
                    name="test",
                    docs_source=source,
                    notebooks_source=notebooks,
                    destination=destination,
                    excluded_source_names=frozenset(
                        {"conf.py", "_templates", "requirements"}
                    ),
                )
            )

            self.assertTrue((destination / "index.md").is_file())
            self.assertTrue((destination / "guide" / "page.rst").is_file())
            self.assertTrue((destination / "_static" / "figure.svg").is_file())
            self.assertTrue((destination / "notebooks" / "README.md").is_file())
            self.assertFalse((destination / "conf.py").exists())
            self.assertFalse((destination / "_templates").exists())
            self.assertFalse((destination / "requirements").exists())
            self.assertFalse((destination / "stale.txt").exists())

    def test_missing_index_does_not_replace_existing_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            destination = root / "staged" / "project"
            source.mkdir()
            destination.mkdir(parents=True)
            (source / "page.md").write_text("# Page\n", encoding="utf-8")
            (destination / "existing.md").write_text("keep\n", encoding="utf-8")

            with self.assertRaises(FileNotFoundError):
                stage_project(
                    StageSpec(name="test", docs_source=source, destination=destination)
                )

            self.assertTrue((destination / "existing.md").is_file())


if __name__ == "__main__":
    unittest.main()
