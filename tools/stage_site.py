#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

DOCS = ROOT / "docs"
STAGED = DOCS / "_staged"

ICS_SRC = ROOT / "zshooter-ics" / "docs" / "source"
DRP_SRC = ROOT / "zshooter-drp" / "docs" / "source"
SIM_SRC = ROOT / "zshooter-sim" / "notebooks"


ICS_DST = STAGED / "ics"
DRP_DST = STAGED / "drp"
SIM_DST = STAGED / "sim" / "notebooks"

def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


import glob


def copy_if_exists(src: Path | str, dst: Path, recurse: bool = False) -> None:
    src_str = str(src)

    # Check if src contains glob patterns
    if any(char in src_str for char in ['*', '?', '[', ']']):
        # Handle glob pattern
        matches = glob.glob(src_str, recursive=recurse)
        if not matches:
            return
            # raise FileNotFoundError(f"No files found matching pattern: {src}")

        # Determine base path for relative structure preservation
        # Find the first part of the path before any glob pattern
        parts = Path(src_str).parts
        base_parts = []
        for part in parts:
            if any(char in part for char in ['*', '?', '[', ']']):
                break
            base_parts.append(part)
        base_path = Path(*base_parts) if base_parts else Path('.')

        for match in matches:
            match_path = Path(match)
            if match_path.is_file():
                # Calculate relative path from base to preserve directory structure
                try:
                    relative = match_path.relative_to(base_path)
                except ValueError:
                    # If relative_to fails, just use the filename
                    relative = match_path.name

                dst_file = dst / relative
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(match_path, dst_file)
    else:
        # Handle single file (original behavior)
        src_path = Path(src) if isinstance(src, str) else src
        if not src_path.exists():
            raise FileNotFoundError(f"Missing required source file: {src_path}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst)


def stage_sim() -> None:
    reset_dir(SIM_DST)

    copy_if_exists(SIM_SRC / "*.rst", SIM_DST)
    copy_if_exists(SIM_SRC / "*.md", SIM_DST)
    copy_if_exists(SIM_SRC / "*.ipynb", SIM_DST)

    # If the ICS docs later gain local _static or image assets, this will bring them along.
    # Safe to keep even if absent.
    for name in ("_static", "_images", "images", "figures"):
        src_dir = ICS_SRC / name
        if src_dir.exists() and src_dir.is_dir():
            shutil.copytree(src_dir, ICS_DST / name, dirs_exist_ok=True)


def stage_ics() -> None:
    reset_dir(ICS_DST)

    copy_if_exists(ICS_SRC / "*.rst", ICS_DST)
    copy_if_exists(ICS_SRC / "*.md", ICS_DST)

    # If the ICS docs later gain local _static or image assets, this will bring them along.
    # Safe to keep even if absent.
    for name in ("_static", "_images", "images", "figures"):
        src_dir = ICS_SRC / name
        if src_dir.exists() and src_dir.is_dir():
            shutil.copytree(src_dir, ICS_DST / name, dirs_exist_ok=True)

def stage_drp() -> None:
    reset_dir(DRP_DST)

    copy_if_exists(DRP_SRC / "*.rst", DRP_DST)
    copy_if_exists(DRP_SRC / "*.md", DRP_DST)

    # If DRP later gains local assets, copy them too.
    for name in ("_static", "_images", "images", "figures"):
        src_dir = DRP_SRC / name
        if src_dir.exists() and src_dir.is_dir():
            shutil.copytree(src_dir, DRP_DST / name, dirs_exist_ok=True)


def main() -> None:
    STAGED.mkdir(parents=True, exist_ok=True)
    stage_ics()
    stage_drp()
    stage_sim()
    print("Staged ICS and DRP documentation into docs/_staged/")


if __name__ == "__main__":
    main()