"""Mirror pages/ and attachments/ from this repo to a OneDrive folder.

Used locally (not in GitHub Actions). One-way: repo -> OneDrive.
Removes files in destination that no longer exist in source.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

MIRROR_DIRS = ("pages", "_meta", "_assets")


def mirror(src: Path, dst: Path) -> dict:
    dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    deleted = 0

    expected: set[Path] = set()
    for sub in MIRROR_DIRS:
        src_sub = src / sub
        if not src_sub.exists():
            continue
        for sf in src_sub.rglob("*"):
            if sf.is_file():
                rel = sf.relative_to(src)
                df = dst / rel
                expected.add(df)
                df.parent.mkdir(parents=True, exist_ok=True)
                if not df.exists() or sf.stat().st_size != df.stat().st_size or sf.stat().st_mtime > df.stat().st_mtime:
                    shutil.copy2(sf, df)
                    copied += 1

    # README
    readme_src = src / "README.md"
    if readme_src.exists():
        readme_dst = dst / "README.md"
        expected.add(readme_dst)
        if not readme_dst.exists() or readme_src.stat().st_mtime > readme_dst.stat().st_mtime:
            shutil.copy2(readme_src, readme_dst)
            copied += 1

    # Prune
    for sub in MIRROR_DIRS:
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
