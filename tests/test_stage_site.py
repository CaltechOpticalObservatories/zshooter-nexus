from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.stage_site import StageSpec, relocate_links, rewrite_markdown_links, stage_project


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

    def test_reports_evidence_and_cross_project_notebook_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sim = root / "sim"
            drp = root / "drp"
            for path in (sim / "docs", sim / "notebooks", sim / "validation" / "data", drp / "docs" / "source", drp / "notebooks"):
                path.mkdir(parents=True)
            (sim / "docs" / "index.md").write_text("# Simulator\n", encoding="utf-8")
            (drp / "docs" / "source" / "index.md").write_text("# DRP\n", encoding="utf-8")
            (drp / "docs" / "source" / "repair.md").write_text("# Repair\n", encoding="utf-8")
            (sim / "validation" / "data" / "values.csv").write_text("x,y\n1,2\n", encoding="utf-8")
            report = "# Report\n[Table](../validation/data/values.csv)\n"
            (sim / "docs" / "report.md").write_text(report, encoding="utf-8")
            notebook = {
                "cells": [
                    {"cell_type": "markdown", "metadata": {}, "source": ["[Report](../docs/report.md#details)\n", "[DRP](../../drp/docs/source/repair.md)\n"]},
                    {"cell_type": "code", "source": ["'[DRP](../../drp/docs/source/repair.md)'"], "metadata": {}, "execution_count": 7, "outputs": [{"output_type": "stream", "name": "stdout", "text": ["saved result\n"]}]},
                ],
                "metadata": {"example": "preserve"}, "nbformat": 4, "nbformat_minor": 5,
            }
            notebook_path = sim / "notebooks" / "example.ipynb"
            notebook_path.write_text(json.dumps(notebook), encoding="utf-8")
            drp_notebook = dict(notebook, cells=[dict(notebook["cells"][0], source="[Repair](../docs/source/repair.md)")])
            (drp / "notebooks" / "example.ipynb").write_text(json.dumps(drp_notebook), encoding="utf-8")
            lock = sim / "stack.toml"
            lock.write_text('revision = "fixed"\n', encoding="utf-8")
            specs = (
                StageSpec(name="sim", docs_source=sim / "docs", docs_subdir=Path("docs"), notebooks_source=sim / "notebooks", destination=root / "published" / "sim", additional_sources=((sim / "validation", Path("validation")), (lock, Path("env/stack.toml")))),
                StageSpec(name="drp", docs_source=drp / "docs" / "source", notebooks_source=drp / "notebooks", destination=root / "published" / "drp"),
            )
            for spec in specs:
                stage_project(spec)
            relocate_links(specs)
            output = root / "published"
            staged = json.loads((output / "sim/notebooks/example.ipynb").read_text())
            self.assertEqual(staged["cells"][0]["source"], ["[Report](../docs/report.md#details)\n", "[DRP](../../drp/repair.md)\n"])
            self.assertEqual(staged["cells"][1], notebook["cells"][1])
            self.assertEqual(staged["metadata"], notebook["metadata"])
            staged_drp = json.loads((output / "drp/notebooks/example.ipynb").read_text())
            self.assertEqual(staged_drp["cells"][0]["source"], "[Repair](../repair.md)")
            self.assertEqual((output / "sim/docs/report.md").read_text(), report)
            self.assertEqual((output / "sim/validation/data/values.csv").read_text(), "x,y\n1,2\n")
            self.assertEqual((output / "sim/env/stack.toml").read_bytes(), lock.read_bytes())
            self.assertEqual(json.loads(notebook_path.read_text()), notebook)
            self.assertEqual((sim / "docs/report.md").read_text(), report)

    def test_link_relocation_preserves_code_examples_and_directives(self) -> None:
        text = (
            "[Report](report.md#section) ![Figure](figure.png)\n"
            "[reference]: report.md \"Title\"\n"
            "`[Example](report.md)`\n"
            "```python\nexample = '[Report](report.md)'\n```\n"
            "```{note}\n[Report](report.md)\n```\n"
            "[After directive](report.md)\n"
        )
        rewritten = rewrite_markdown_links(text, lambda url: "moved/" + url)
        self.assertIn("[Report](moved/report.md#section)", rewritten)
        self.assertIn("![Figure](moved/figure.png)", rewritten)
        self.assertIn('[reference]: moved/report.md "Title"', rewritten)
        self.assertIn("`[Example](report.md)`", rewritten)
        self.assertIn("example = '[Report](report.md)'", rewritten)
        self.assertIn("```{note}\n[Report](moved/report.md)\n```", rewritten)
        self.assertIn("[After directive](moved/report.md)", rewritten)


if __name__ == "__main__":
    unittest.main()
