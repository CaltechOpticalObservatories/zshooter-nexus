from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.stage_site import StageSpec, portable_paths, prepare_publication, relocate_links, rewrite_markdown_links, stage_project


class StageProjectTests(unittest.TestCase):
    def test_navigation_selects_pages_and_keeps_repository_records_off_site(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "sim"
            site = root / "site"
            for path in (repo / "docs", repo / "notebooks", repo / "validation", site / "simulator"):
                path.mkdir(parents=True)
            (repo / "docs/index.md").write_text("# Repository index\n")
            (repo / "docs/report.md").write_text("# Report\n[Debug run](../validation/debug.ipynb#results)\n![Figure](../validation/figure.svg)\n")
            notebook = '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}'
            (repo / "notebooks/science.ipynb").write_text(notebook)
            (repo / "notebooks/unlisted.ipynb").write_text(notebook)
            (repo / "validation/debug.ipynb").write_text(notebook)
            (repo / "validation/figure.svg").write_text("<svg/>\n")
            navigation = site / "simulator/science.rst"
            navigation.write_text(".. toctree::\n\n   Science </_staged/sim/notebooks/science>\n   Report </_staged/sim/docs/report>\n")
            spec = StageSpec(name="sim", docs_source=repo / "docs", docs_subdir=Path("docs"), notebooks_source=repo / "notebooks", destination=site / "_staged/sim", require_index=False, additional_sources=((repo / "validation", Path("validation")),), navigation_source=site, repository_source=repo, repository_url="https://github.com/example/sim/blob/main")
            stage_project(spec)
            relocate_links((spec,))
            self.assertTrue((spec.destination / "notebooks/science.ipynb").exists())
            self.assertTrue((spec.destination / "_downloads/notebooks/science.ipynb").exists())
            for name in ("docs/index.md", "notebooks/unlisted.ipynb", "validation/debug.ipynb", "_downloads/validation/debug.ipynb"):
                self.assertFalse((spec.destination / name).exists())
            self.assertEqual((spec.destination / "validation/figure.svg").read_text(), "<svg/>\n")
            self.assertIn("https://github.com/example/sim/blob/main/validation/debug.ipynb#results", (spec.destination / "docs/report.md").read_text())
            self.assertIn("![Figure](../validation/figure.svg)", (spec.destination / "docs/report.md").read_text())
            self.assertEqual((repo / "validation/debug.ipynb").read_text(), notebook)

            # A source rename gives an actionable error and preserves the last
            # publication; updating that one navigation entry repairs the build.
            (repo / "notebooks/science.ipynb").rename(repo / "notebooks/renamed.ipynb")
            with self.assertRaisesRegex(FileNotFoundError, "Update sim site navigation.*notebooks/science"):
                stage_project(spec)
            self.assertTrue((spec.destination / "notebooks/science.ipynb").exists())
            navigation.write_text(navigation.read_text().replace("notebooks/science", "notebooks/renamed"))
            stage_project(spec)
            self.assertTrue((spec.destination / "notebooks/renamed.ipynb").exists())
            self.assertFalse((spec.destination / "notebooks/science.ipynb").exists())
            self.assertFalse((spec.destination / "_downloads/notebooks/science.ipynb").exists())

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

    def test_published_logs_and_downloads_are_portable_without_changing_results(self):
        notebook = {
            "cells": [
                {"cell_type": "markdown", "source": ["[Report](../docs/report.md)\n"], "metadata": {}},
                {"cell_type": "code", "source": ["print(output_dir)\n"], "execution_count": 17, "metadata": {}, "outputs": [
                    {"output_type": "stream", "name": "stdout", "text": ["Products: /Users/observer/src/zs-scopesim/notebooks/results\n", "S/N: 42.5\n"]},
                    {"output_type": "display_data", "data": {"text/html": "<pre>/home/observer/src/irdb/ZShooter_v2</pre>", "image/png": "unchanged-image-data", "application/json": {"flux": [1.5, 2.3]}}, "metadata": {}},
                ]},
            ], "metadata": {}, "nbformat": 4, "nbformat_minor": 5,
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "notebooks").mkdir()
            (root / "notebooks/example.ipynb").write_text(json.dumps(notebook), encoding="utf-8")
            (root / "profile.txt").write_text("/Users/observer/miniforge3/envs/zssim/lib/python3.14/site-packages/numpy/core.py:10 0.125\n", encoding="utf-8")
            prepare_publication(root)
            staged = json.loads((root / "notebooks/example.ipynb").read_text())
            self.assertEqual(staged["cells"][1]["source"], notebook["cells"][1]["source"])
            self.assertEqual(staged["cells"][1]["execution_count"], 17)
            self.assertEqual(staged["cells"][1]["outputs"][0]["text"], ["Products: zs-scopesim/notebooks/results\n", "S/N: 42.5\n"])
            self.assertEqual(staged["cells"][1]["outputs"][1]["data"]["image/png"], "unchanged-image-data")
            self.assertEqual(staged["cells"][1]["outputs"][1]["data"]["application/json"], {"flux": [1.5, 2.3]})
            self.assertEqual(staged["cells"][1]["outputs"][1]["data"]["text/html"], "<pre>irdb/ZShooter_v2</pre>")
            self.assertEqual(json.loads((root / "_downloads/notebooks/example.ipynb").read_text()), staged)
            self.assertEqual(staged["cells"][0], notebook["cells"][0])
            self.assertEqual((root / "profile.txt").read_text(), "python-environment/lib/python3.14/site-packages/numpy/core.py:10 0.125\n")

    def test_personal_code_path_is_rejected_without_replacing_previous_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "notebooks"
            destination = root / "staged"
            source.mkdir()
            destination.mkdir()
            (destination / "existing.txt").write_text("keep", encoding="utf-8")
            notebook = {"cells": [{"cell_type": "code", "source": ['path = "/Users/observer/src/irdb"']} ]}
            original = json.dumps(notebook)
            (source / "example.ipynb").write_text(original, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "portable path"):
                stage_project(StageSpec(name="test", notebooks_source=source, destination=destination, require_index=False))
            self.assertEqual((destination / "existing.txt").read_text(), "keep")
            self.assertEqual((source / "example.ipynb").read_text(), original)

    def test_other_checkout_layouts_and_ordinary_text(self):
        self.assertEqual(portable_paths("/Users/observer/Desktop/ZShooter/ScopeSim/scopesim/example.py:170"), "ScopeSim/scopesim/example.py:170")
        self.assertEqual(portable_paths("/Users/observer/Desktop/ZShooter/.venv/lib/python3.12/test.py"), "python-environment/lib/python3.12/test.py")
        self.assertEqual(portable_paths("/home/observer/.cache/test.fits"), "~/.cache/test.fits")
        self.assertEqual(portable_paths("https://example.org/report 3.14159 notebooks/result.fits"), "https://example.org/report 3.14159 notebooks/result.fits")


if __name__ == "__main__":
    unittest.main()
