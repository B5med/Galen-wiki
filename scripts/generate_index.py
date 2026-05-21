"""Generate GalenMD/_Index.md — hierarchical page index with freshness indicators.

Reads _meta/index.json, builds the Confluence page tree, and writes
GalenMD/_Index.md with wikilinks, version numbers, last-update dates,
and freshness emoji.

Usage
-----
    python scripts/generate_index.py [--out REPO_ROOT] [--galenmd GALENMD_DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Freshness thresholds ───────────────────────────────────────────────────────
# (max_days, emoji, label_cs)   — ordered from freshest to oldest
FRESHNESS: list[tuple[int | None, str, str]] = [
    (3,    "🔥", "do 3 dnů"),
    (14,   "♨️",  "do 14 dnů"),
    (30,   "🌿",  "do 30 dnů"),
    (90,   "📄",  "do 90 dnů"),
    (None, "🗄️",  "starší než 3 měsíce"),
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def format_date(d: date) -> str:
    """Return Czech-style date without leading zeros, e.g. '7. 5. 2026'."""
    return f"{d.day}. {d.month}. {d.year}"


def freshness(updated_at: str, today: date) -> tuple[str, str, int]:
    """Return (emoji, formatted_date, age_days) for an ISO datetime string."""
    if not updated_at:
        return "❓", "—", -1
    try:
        dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        d = dt.date()
        age = (today - d).days
    except (ValueError, TypeError):
        return "❓", updated_at[:10], -1

    for max_days, emoji, _ in FRESHNESS:
        if max_days is None or age <= max_days:
            return emoji, format_date(d), age
    return "🗄️", format_date(d), age   # fallback (should never reach here)


def build_children_map(pages: dict) -> dict[str | None, list[str]]:
    """Build {parent_id → [child_id, …]} map.

    Pages whose parent is not in the local index are treated as roots (their
    parent lives in a different Confluence space or above our sync boundary).
    """
    children: dict[str | None, list[str]] = {}
    for pid, info in pages.items():
        parent = info.get("parent_id") or None
        if parent and parent not in pages:
            parent = None          # orphan — elevate to root
        children.setdefault(parent, []).append(pid)

    # Sort each sibling list: sections (with children) first, then leaves,
    # both groups alphabetically.
    for lst in children.values():
        lst.sort(key=lambda pid: (
            0 if pid in children else 1,
            pages[pid].get("title", "").lower(),
        ))
    return children


def render_node(
    page_id: str,
    pages: dict,
    children: dict,
    today: date,
    depth: int,
    lines: list[str],
) -> None:
    info = pages[page_id]
    title = info["title"]
    path_name = Path(info["path"]).name     # safe_filename version
    version = info.get("version", "?")
    updated = info.get("updated_at", "")
    emoji, date_str, _age = freshness(updated, today)

    indent = "  " * depth
    link = f"[[{path_name}|{title}]]" if path_name != title else f"[[{title}]]"

    # Bold pages that have sub-pages (act as sections)
    if page_id in children:
        page_part = f"**{link}**"
    else:
        page_part = link

    lines.append(f"{indent}- {emoji} {page_part} `v{version}` · {date_str}")

    for child_id in children.get(page_id, []):
        render_node(child_id, pages, children, today, depth + 1, lines)


def age_stats(pages: dict, today: date) -> dict[str, int]:
    counts: Counter = Counter()
    for info in pages.values():
        updated = info.get("updated_at", "")
        emoji, _, _ = freshness(updated, today)
        counts[emoji] += 1
    return dict(counts)


# ── Main generator ────────────────────────────────────────────────────────────

def generate_index(out_root: Path, galenmd_root: Path) -> Path:
    today = date.today()

    idx_path = out_root / "_meta" / "index.json"
    if not idx_path.exists():
        raise FileNotFoundError(f"_meta/index.json not found in {out_root}")

    data = json.loads(idx_path.read_text(encoding="utf-8"))
    pages: dict = data.get("pages", {})
    synced_at = data.get("synced_at", "")[:10]
    total = len(pages)

    children = build_children_map(pages)
    stats = age_stats(pages, today)

    # ── Build document ────────────────────────────────────────────────────────
    lines: list[str] = []

    # Frontmatter
    lines += [
        "---",
        'title: "Rejstřík stránek FONS Galen"',
        f"generated: {today.isoformat()}",
        "---",
        "",
    ]

    # Title + summary
    lines += [
        "# 📚 Rejstřík stránek FONS Galen",
        "",
        f"> **{format_date(today)}**  ·  Celkem stránek: **{total}**  ·  Poslední sync z Confluence: {synced_at}",
        "",
    ]

    # Legend table
    lines += [
        "## Legenda stáří dokumentu",
        "",
        "| Emoji | Stáří | Počet |",
        "|:-----:|-------|:-----:|",
    ]
    for _, emoji, label in FRESHNESS:
        count = stats.get(emoji, 0)
        lines.append(f"| {emoji} | {label.capitalize()} | **{count}** |")
    lines.append(f"| ❓ | Bez data | **{stats.get('❓', 0)}** |")

    # Section intro
    lines += [
        "",
        "---",
        "",
        "## Hierarchický přehled",
        "",
        "> `emoji` **Sekce** / stránka  `verze`  ·  datum poslední aktualizace",
        "",
    ]

    # Tree — render each root
    tree_lines: list[str] = []
    for root_id in children.get(None, []):
        render_node(root_id, pages, children, today, 0, tree_lines)

    lines.extend(tree_lines)
    lines.append("")

    # Write
    galenmd_root.mkdir(parents=True, exist_ok=True)
    out_path = galenmd_root / "_Index.md"
    out_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"Index vygenerován → {out_path.name}  ({total} stránek, {format_date(today)})")
    return out_path


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="Generate hierarchical page index for Obsidian")
    ap.add_argument("--out",     default=".",        help="Repo root (contains _meta/)")
    ap.add_argument("--galenmd", default="GalenMD",  help="Output directory (default: GalenMD)")
    args = ap.parse_args()

    out_root    = Path(args.out).resolve()
    galenmd_dir = (
        Path(args.galenmd) if Path(args.galenmd).is_absolute()
        else out_root / args.galenmd
    )

    try:
        generate_index(out_root, galenmd_dir)
    except FileNotFoundError as e:
        print(f"CHYBA: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
