"""Mirror GalenMD/ from this repo to a OneDrive folder.

Used locally (not in GitHub Actions). One-way: repo -> OneDrive.
Removes files in destination that no longer exist in source.

What is mirrored:
  GalenMD/     — all Markdown files (complete)
  pages/**/assets/**  — images and attachments only (HTML/JSON stays in git)

GalenMD Markdown files reference images via relative paths pointing into pages/
(e.g. "../../../pages/.../assets/image.png"), so both directories must be present
side-by-side on OneDrive for the links to resolve correctly.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

MIRROR_DIRS = ("GalenMD",)
# From pages/ only files that live inside an 'assets' subdirectory are copied.
ASSET_MIRROR_DIRS = ("pages",)


def _copy_if_newer(sf: Path, df: Path) -> bool:
    """Copy sf → df when df is missing or outdated. Returns True if copied."""
    if not df.exists() or sf.stat().st_size != df.stat().st_size or sf.stat().st_mtime > df.stat().st_mtime:
        df.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sf, df)
        return True
    return False


def mirror(src: Path, dst: Path) -> dict:
    dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    deleted = 0

    expected: set[Path] = set()

    # 1. Full mirror of GalenMD/
    for sub in MIRROR_DIRS:
        src_sub = src / sub
        if not src_sub.exists():
            continue
        for sf in src_sub.rglob("*"):
            if sf.is_file():
                rel = sf.relative_to(src)
                df = dst / rel
                expected.add(df)
                if _copy_if_newer(sf, df):
                    copied += 1

    # 2. Assets-only mirror from pages/
    for sub in ASSET_MIRROR_DIRS:
        src_sub = src / sub
        if not src_sub.exists():
            continue
        for sf in src_sub.rglob("*"):
            if not sf.is_file():
                continue
            # Only files inside an 'assets' folder (at any depth)
            rel_parts = sf.relative_to(src_sub).parts
            if "assets" not in rel_parts:
                continue
            rel = sf.relative_to(src)
            df = dst / rel
            expected.add(df)
            if _copy_if_newer(sf, df):
                copied += 1

    # README
    readme_src = src / "README.md"
    if readme_src.exists():
        readme_dst = dst / "README.md"
        expected.add(readme_dst)
        if _copy_if_newer(readme_src, readme_dst):
            copied += 1

    # 3. Prune files no longer in source (GalenMD + pages assets)
    for sub in (*MIRROR_DIRS, *ASSET_MIRROR_DIRS):
        dst_sub = dst / sub
        if not dst_sub.exists():
            continue
        for df in dst_sub.rglob("*"):
            if df.is_file() and df not in expected:
                df.unlink()
                deleted += 1
        for d in sorted((p for p in dst_sub.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
            try:
                d.rmdir()
            except OSError:
                pass

    return {"copied": copied, "deleted": deleted, "dest": str(dst)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=".", help="Repo root")
    ap.add_argument("--dst", required=True, help="OneDrive destination folder")
    args = ap.parse_args()
    res = mirror(Path(args.src).resolve(), Path(args.dst).resolve())
    print(res)
    return 0


if __name__ == "__main__":
    sys.exit(main())
