"""Sync Confluence space `fg` (FONS Galen) to local archive.

Each page becomes a directory containing:
  - index.html         (export_view, with rewritten asset links)
  - source.xhtml       (storage format - canonical source)
  - content.adf.json   (atlas_doc_format - structured)
  - meta.json          (id, title, version, ...)
  - assets/            (images and attachments)

Designed for anonymous access; idempotent; version-cached for fast re-runs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urljoin, urlparse

import warnings

import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

HOST = "https://stapro-galen.atlassian.net"
BASE = f"{HOST}/wiki"
SPACE_KEY = "fg"
USER_AGENT = "Galen-wiki-archive/2.0 (+https://github.com/B5med/Galen-wiki)"
TIMEOUT = 30
RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_RETRIES = 5


class Confluence:
    def __init__(self) -> None:
        self.s = requests.Session()
        self.s.headers["User-Agent"] = USER_AGENT
        self.s.headers["Accept"] = "application/json"

    def get_json(self, url: str, params: dict | None = None) -> dict:
        for attempt in range(MAX_RETRIES):
            r = self.s.get(url, params=params, timeout=TIMEOUT)
            if r.status_code in RETRY_STATUS:
                wait = int(r.headers.get("Retry-After", 2**attempt))
                print(f"  retry {attempt + 1}/{MAX_RETRIES} after {wait}s (status {r.status_code})", file=sys.stderr)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError(f"giving up on {url}")

    def get_binary(self, url: str) -> bytes | None:
        for attempt in range(MAX_RETRIES):
            r = self.s.get(url, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code in (404, 410):
                return None
            if r.status_code in RETRY_STATUS:
                wait = int(r.headers.get("Retry-After", 2**attempt))
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.content
        raise RuntimeError(f"giving up on {url}")

    def paginate(self, url: str, params: dict | None = None) -> Iterator[dict]:
        next_url: str | None = url
        next_params = params
        while next_url:
            data = self.get_json(next_url, next_params)
            yield from data.get("results", [])
            nxt = data.get("_links", {}).get("next")
            if nxt:
                next_url = nxt if nxt.startswith("http") else urljoin(HOST, nxt)
                next_params = None
            else:
                next_url = None


# ---------- helpers ----------

_FORBIDDEN = re.compile(r'[<>:"/\\|?*\x00-\x1f]+')
_TRIM = re.compile(r"\s+")
_RESERVED = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}


def safe_filename(s: str, max_len: int = 120) -> str:
    """Sanitize for Windows + POSIX filesystem. Preserves Unicode (diacritics)."""
    if not s:
        return "untitled"
    s = _FORBIDDEN.sub("_", s)
    s = _TRIM.sub(" ", s).strip().strip(".")
    if s.upper() in _RESERVED:
        s = "_" + s
    return s[:max_len] or "untitled"


def get_space_id(c: Confluence, key: str) -> str:
    data = c.get_json(f"{BASE}/api/v2/spaces", params={"keys": key})
    results = data.get("results", [])
    if not results:
        raise RuntimeError(f"space {key!r} not found")
    return results[0]["id"]


def build_page_dir(page: dict, by_id: dict[str, dict]) -> Path:
    """Return Path like 'Parent/Child/Grandchild' (relative to pages/)."""
    parts: list[str] = []
    cur = page
    seen: set[str] = set()
    while cur is not None and cur["id"] not in seen:
        seen.add(cur["id"])
        parts.append(safe_filename(cur.get("title") or cur["id"]))
        parent_id = cur.get("parentId")
        cur = by_id.get(parent_id) if parent_id else None
    parts.reverse()
    return Path(*parts) if parts else Path("untitled")


def load_cache(out_root: Path) -> dict[str, dict]:
    """Load previous _meta/index.json mapping page_id -> {version, path, ...}."""
    idx = out_root / "_meta" / "index.json"
    if not idx.exists():
        return {}
    try:
        data = json.loads(idx.read_text(encoding="utf-8"))
        return data.get("pages", {}) or {}
    except Exception:
        return {}


def _lp(p: Path) -> Path:
    """Na Windows pouzij prefix \\?\ pro obejiti limitu 260 znaku v cestach."""
    if sys.platform != "win32":
        return p
    s = str(p.resolve())
    return Path(s) if s.startswith("\\\\?\\") else Path("\\\\?\\" + s)


def write_text(path: Path, content: str) -> bool:
    lp = _lp(path)
    lp.parent.mkdir(parents=True, exist_ok=True)
    if lp.exists() and lp.read_text(encoding="utf-8") == content:
        return False
    lp.write_text(content, encoding="utf-8", newline="\n")
    return True


def write_bytes(path: Path, content: bytes) -> bool:
    lp = _lp(path)
    lp.parent.mkdir(parents=True, exist_ok=True)
    if lp.exists() and lp.read_bytes() == content:
        return False
    lp.write_bytes(content)
    return True


# ---------- Storage XHTML helpers ----------

def extract_panel_icons(storage_xhtml: str) -> dict[str, str]:
    """Return mapping of panel first-text → icon emoji from Confluence storage XHTML.

    Handles <ac:structured-macro ac:name="panel"> blocks that carry
    <ac:parameter ac:name="panelIconText">▶️</ac:parameter>.
    """
    if not storage_xhtml or "panelIconText" not in storage_xhtml:
        return {}
    soup = BeautifulSoup(storage_xhtml, "html.parser")
    result: dict[str, str] = {}
    for macro in soup.find_all(attrs={"ac:name": "panel"}):
        icon_param = macro.find(attrs={"ac:name": "panelIconText"})
        if not icon_param:
            continue
        icon = icon_param.get_text(strip=True)
        if not icon:
            continue
        # Get first non-empty text inside the rich-text-body
        body = macro.find("ac:rich-text-body")
        if not body:
            continue
        first_text = body.get_text(separator=" ", strip=True)[:80]
        if first_text:
            result[first_text] = icon
    return result


def inject_panel_icons(export_html: str, panel_icons: dict[str, str]) -> str:
    """Prepend icon emoji to matching <div class="panelContent"> elements."""
    if not panel_icons or not export_html:
        return export_html
    soup = BeautifulSoup(export_html, "html.parser")
    for div in soup.find_all("div", class_="panelContent"):
        text = div.get_text(separator=" ", strip=True)[:80]
        for key, icon in panel_icons.items():
            if key and text and (key[:30] in text or text[:30] in key):
                first_p = div.find("p")
                if first_p:
                    span = soup.new_tag("span", attrs={"class": "panel-icon"})
                    span.string = icon + " "
                    first_p.insert(0, span)
                break
    return str(soup)


# ---------- HTML asset rewriting ----------

ASSET_URL_RE = re.compile(
    r"/wiki/download/(?:attachments|thumbnails)/(?P<page>\d+)/(?P<filename>[^?#]+)"
)


def extract_filename_from_url(url: str) -> str | None:
    """Return URL-decoded filename if URL points at a download attachment."""
    m = ASSET_URL_RE.search(url)
    if not m:
        return None
    return unquote(m.group("filename"))


def rewrite_html(html: str, asset_map: dict[str, str]) -> str:
    """Rewrite asset URLs to local paths and replace emoji <img> with unicode fallback.

    asset_map: URL-decoded original filename -> local sanitized filename.
    """
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")

    # Replace empty AUI icon spans in info macros with unicode equivalents
    MACRO_ICONS = {
        "confluence-information-macro-information": "ℹ️",
        "confluence-information-macro-tip":         "💡",
        "confluence-information-macro-note":        "⚠️",
        "confluence-information-macro-warning":     "🚫",
    }
    for span in soup.find_all("span", class_="confluence-information-macro-icon"):
        classes = span.get("class", [])
        icon = "ℹ️"
        parent = span.parent
        if parent:
            parent_classes = parent.get("class", [])
            for cls, ico in MACRO_ICONS.items():
                if cls in parent_classes:
                    icon = ico
                    break
        span.string = icon
        span["style"] = "font-family:'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif;margin-right:6px;flex-shrink:0"

    # Replace Confluence emoji <img class="emoticon"> with unicode character from data-emoji-fallback
    for tag in soup.find_all("img", class_="emoticon"):
        fallback = tag.get("data-emoji-fallback") or tag.get("alt", "")
        span = soup.new_tag("span", attrs={"class": "emoji", "title": tag.get("data-emoji-shortname", "")})
        span.string = fallback
        tag.replace_with(span)

    # Rewrite attachment/thumbnail URLs to local assets
    attrs = [("img", "src"), ("a", "href"), ("source", "src"), ("video", "src"), ("video", "poster"), ("audio", "src"), ("embed", "src")]
    for tag_name, attr in attrs:
        for tag in soup.find_all(tag_name):
            val = tag.get(attr)
            if not val:
                continue
            original_fn = extract_filename_from_url(val)
            if original_fn and original_fn in asset_map:
                tag[attr] = f"./assets/{asset_map[original_fn]}"
    return str(soup)


# ---------- per-page save ----------

HTML_WRAPPER = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="canonical" href="{source_url}">
<link rel="stylesheet" href="{css_path}">
</head>
<body>
<header><h1>{title}</h1><p><small><a href="{source_url}">Source</a> · version {version} · updated {updated_at}</small></p></header>
<main>
{body}
</main>
</body>
</html>
"""


def css_rel_path(page_dir: Path, out_root: Path) -> str:
    """Compute relative path from page_dir/index.html to _assets/confluence.css."""
    depth = len(page_dir.relative_to(out_root / "pages").parts)
    return "../" * (depth + 1) + "_assets/confluence.css"


def save_page(
    page_dir: Path,
    page_id: str,
    title: str,
    version: int | None,
    updated_at: str | None,
    author_id: str | None,
    parent_id: str | None,
    storage_html: str,
    export_view_html: str,
    adf_value: Any,
    attachments_meta: list[dict],
    asset_map: dict[str, str],
    out_root: Path,
) -> int:
    """Write all per-page files. Returns count of files actually changed."""
    changed = 0
    source_url = f"{BASE}/spaces/{SPACE_KEY}/pages/{page_id}"

    # index.html with rewritten asset links and panel icons from storage
    panel_icons = extract_panel_icons(storage_html or "")
    rewritten_body = rewrite_html(export_view_html or "", asset_map)
    rewritten_body = inject_panel_icons(rewritten_body, panel_icons)
    html_doc = HTML_WRAPPER.format(
        title=html_escape(title),
        source_url=html_escape(source_url),
        version=version,
        updated_at=html_escape(updated_at or ""),
        body=rewritten_body,
        css_path=css_rel_path(page_dir, out_root),
    )
    if write_text(page_dir / "index.html", html_doc):
        changed += 1

    # source.xhtml - canonical storage
    storage_doc = (
        f'<?xml version="1.0" encoding="utf-8"?>\n'
        f'<page id="{html_escape(page_id)}" version="{version}" '
        f'updated_at="{html_escape(updated_at or "")}" '
        f'source="{html_escape(source_url)}"\n'
        f'  xmlns:ac="http://atlassian.com/content"\n'
        f'  xmlns:ri="http://atlassian.com/resource/identifier">\n'
        f'<title>{html_escape(title)}</title>\n'
        f'<body>{storage_html or ""}</body>\n'
        f'</page>\n'
    )
    if write_text(page_dir / "source.xhtml", storage_doc):
        changed += 1

    # content.adf.json
    adf_text = json.dumps(adf_value if adf_value is not None else {}, ensure_ascii=False, indent=2) + "\n"
    if write_text(page_dir / "content.adf.json", adf_text):
        changed += 1

    # meta.json
    meta = {
        "id": page_id,
        "title": title,
        "version": version,
        "updated_at": updated_at,
        "author_id": author_id,
        "parent_id": parent_id,
        "source": source_url,
        "attachments": attachments_meta,
    }
    meta_text = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
    if write_text(page_dir / "meta.json", meta_text):
        changed += 1

    return changed


def html_escape(s: str) -> str:
    return (
        str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    )


# ---------- main sync ----------

EXPECTED_FILES = ("index.html", "source.xhtml", "content.adf.json", "meta.json")


def sync(out_root: Path) -> dict:
    c = Confluence()
    pages_root = out_root / "pages"
    meta_dir = out_root / "_meta"
    meta_dir.mkdir(parents=True, exist_ok=True)

    cache = load_cache(out_root)
    print(f"Loaded {len(cache)} pages from cache")

    print(f"Resolving space {SPACE_KEY!r}...")
    space_id = get_space_id(c, SPACE_KEY)
    print(f"Space id: {space_id}")

    print("Listing pages...")
    raw_pages = list(
        c.paginate(
            f"{BASE}/api/v2/spaces/{space_id}/pages",
            params={"limit": 250, "status": "current"},
        )
    )
    by_id = {p["id"]: p for p in raw_pages}
    print(f"Found {len(raw_pages)} pages")

    expected_dirs: set[Path] = set()
    index_pages: dict[str, dict] = {}
    stats = {"total": len(raw_pages), "updated": 0, "new": 0, "skipped": 0, "files_changed": 0}

    for i, summary in enumerate(raw_pages, 1):
        page_id = summary["id"]
        title = summary.get("title") or page_id
        current_version = (summary.get("version") or {}).get("number")

        rel_dir = build_page_dir(summary, by_id)
        page_dir = pages_root / rel_dir
        # Disambiguate path collisions (rare: two pages with same title under same parent)
        if page_dir in expected_dirs:
            page_dir = page_dir.parent / f"{page_dir.name} ({page_id})"
        expected_dirs.add(page_dir)

        cached = cache.get(page_id)
        all_files_present = page_dir.exists() and all((page_dir / f).exists() for f in EXPECTED_FILES)
        is_unchanged = (
            cached
            and cached.get("version") == current_version
            and cached.get("path") == str(page_dir.relative_to(out_root)).replace("\\", "/")
            and all_files_present
        )

        if is_unchanged:
            print(f"[{i}/{len(raw_pages)}] {title} (skipped, v{current_version} unchanged)")
            stats["skipped"] += 1
            # carry forward cached entry so we don't lose it from index
            index_pages[page_id] = {
                "title": title,
                "version": current_version,
                "updated_at": cached.get("updated_at"),
                "author_id": cached.get("author_id"),
                "parent_id": summary.get("parentId"),
                "path": str(page_dir.relative_to(out_root)).replace("\\", "/"),
            }
            continue

        action = "new" if not cached else f"updating v{cached.get('version')} -> v{current_version}"
        print(f"[{i}/{len(raw_pages)}] {title} ({action})")
        if not cached:
            stats["new"] += 1
        else:
            stats["updated"] += 1

        # Fetch all three body formats (3 calls)
        storage_html = ""
        export_view_html = ""
        adf_value: Any = None
        version: int | None = current_version
        updated_at: str | None = None
        author_id: str | None = None

        for fmt, dest in (("storage", "storage"), ("export_view", "export_view"), ("atlas_doc_format", "atlas_doc_format")):
            data = c.get_json(f"{BASE}/api/v2/pages/{page_id}", params={"body-format": fmt})
            body = (data.get("body") or {}).get(dest, {})
            v = body.get("value")
            if fmt == "storage":
                storage_html = v or ""
            elif fmt == "export_view":
                export_view_html = v or ""
            else:
                if isinstance(v, str):
                    try:
                        adf_value = json.loads(v)
                    except json.JSONDecodeError:
                        adf_value = v
                else:
                    adf_value = v
            # version metadata from any response
            ver = data.get("version") or {}
            if version is None:
                version = ver.get("number")
            updated_at = updated_at or ver.get("createdAt")
            author_id = author_id or ver.get("authorId")

        # Attachments
        page_assets_dir = page_dir / "assets"
        attachments_meta: list[dict] = []
        asset_map: dict[str, str] = {}
        used_names: set[str] = set()

        for att in c.paginate(
            f"{BASE}/api/v2/pages/{page_id}/attachments",
            params={"limit": 250},
        ):
            att_title = att.get("title") or att["id"]
            download = att.get("downloadLink") or (att.get("_links") or {}).get("download")
            if not download:
                continue
            if download.startswith("http"):
                url = download
            else:
                path = download if download.startswith("/wiki/") else f"/wiki{download if download.startswith('/') else '/' + download}"
                url = urljoin(HOST, path)
            data_bytes = c.get_binary(url)
            if data_bytes is None:
                print(f"  skipped attachment (404): {att_title}", file=sys.stderr)
                continue

            local_name = safe_filename(att_title)
            # Ensure unique within page
            base, dot, ext = local_name.rpartition(".")
            stem = base if dot else local_name
            suffix = f".{ext}" if dot else ""
            n = 1
            unique = local_name
            while unique in used_names:
                n += 1
                unique = f"{stem} ({n}){suffix}"
            used_names.add(unique)

            att_path = page_assets_dir / unique
            if write_bytes(att_path, data_bytes):
                stats["files_changed"] += 1

            asset_map[att_title] = unique  # for HTML rewriting
            attachments_meta.append({
                "id": att.get("id"),
                "title": att_title,
                "mediaType": att.get("mediaType"),
                "fileSize": att.get("fileSize"),
                "version": (att.get("version") or {}).get("number"),
                "local": f"assets/{unique}",
            })

        changed = save_page(
            page_dir=page_dir,
            page_id=page_id,
            title=title,
            version=version,
            updated_at=updated_at,
            author_id=author_id,
            parent_id=summary.get("parentId"),
            storage_html=storage_html,
            export_view_html=export_view_html,
            adf_value=adf_value,
            attachments_meta=attachments_meta,
            asset_map=asset_map,
            out_root=out_root,
        )
        stats["files_changed"] += changed

        index_pages[page_id] = {
            "title": title,
            "version": version,
            "updated_at": updated_at,
            "author_id": author_id,
            "parent_id": summary.get("parentId"),
            "path": str(page_dir.relative_to(out_root)).replace("\\", "/"),
        }

    # Sort index by title for stable diffs
    index_pages = dict(sorted(index_pages.items(), key=lambda kv: (kv[1]["title"] or "").lower()))

    # Prune deleted pages
    removed = 0
    if pages_root.exists():
        for p in pages_root.rglob("meta.json"):
            page_dir = p.parent
            if page_dir not in expected_dirs:
                # remove entire page dir
                for f in page_dir.rglob("*"):
                    if f.is_file():
                        f.unlink()
                removed += 1
        # Remove empty dirs bottom-up
        for d in sorted((p for p in pages_root.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
            try:
                d.rmdir()
            except OSError:
                pass

    stats["removed"] = removed

    index_doc = {
        "space_id": space_id,
        "space_key": SPACE_KEY,
        "synced_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pages": index_pages,
    }
    write_text(meta_dir / "index.json", json.dumps(index_doc, ensure_ascii=False, indent=2) + "\n")

    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=".", help="Output root (repo root)")
    ap.add_argument("--github-output", default=None, help="Path to GITHUB_OUTPUT file (CI)")
    args = ap.parse_args()
    out = Path(args.out).resolve()
    stats = sync(out)
    print("\n" + json.dumps(stats, indent=2))

    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as f:
            f.write(f"total={stats['total']}\n")
            f.write(f"updated={stats['updated']}\n")
            f.write(f"new={stats['new']}\n")
            f.write(f"removed={stats['removed']}\n")
            f.write(f"skipped={stats['skipped']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
