#!/usr/bin/env python3
"""Search Unsplash for retro/vintage landscape candidates.

Writes <output_dir>/_candidates.json (used by preview.py and download.py) and
prints a short summary. Does NOT fire any download-tracking pings — previews
are hotlinks and count as views automatically. Read SKILL.md and
references/unsplash-compliance.md before changing this file.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_BASE = "https://api.unsplash.com"
DEFAULT_OUTPUT_DIR = "content-workspace/_assets"
DEFAULT_SEED = "retro vintage"
DEFAULT_ORIENTATION = "landscape"
DEFAULT_CONTENT_FILTER = "low"
DEFAULT_PER_PAGE = 6
CANDIDATES_FILENAME = "_candidates.json"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def require_env() -> tuple[str, str]:
    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    app = os.environ.get("UNSPLASH_APP_NAME")
    missing = [n for n, v in (("UNSPLASH_ACCESS_KEY", key), ("UNSPLASH_APP_NAME", app)) if not v]
    if missing:
        die(
            f"missing env var(s): {', '.join(missing)}.\n"
            "  Set them in ~/.zshrc and `source` it:\n"
            "    export UNSPLASH_ACCESS_KEY=\"...\"   # from https://unsplash.com/oauth/applications\n"
            "    export UNSPLASH_APP_NAME=\"aaronheld-blog\""
        )
    return key, app  # type: ignore[return-value]


def _request(url: str, *, key: str) -> tuple[dict | list, dict]:
    """Authorized GET against api.unsplash.com. Returns (json_body, response_headers)."""
    req = urllib.request.Request(url, headers={
        "Authorization": f"Client-ID {key}",
        "Accept-Version": "v1",
        "User-Agent": "unsplash-retro-landscape/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        if e.code == 401:
            die("401 from Unsplash — UNSPLASH_ACCESS_KEY is missing or invalid.\n"
                "  Check it at https://unsplash.com/oauth/applications")
        if e.code == 403:
            die(f"403 from Unsplash — likely rate limit hit. Response: {detail}")
        if e.code == 404:
            die(f"404 from Unsplash — resource not found. URL: {url}")
        die(f"HTTP {e.code} from Unsplash: {detail}")
    except urllib.error.URLError as e:
        die(f"network error reaching Unsplash: {e}")


def search(query: str, *, orientation: str, color: str | None, content_filter: str,
           per_page: int, page: int, order_by: str, key: str) -> tuple[list[dict], dict]:
    params = {
        "query": query,
        "orientation": orientation,
        "content_filter": content_filter,
        "per_page": str(per_page),
        "page": str(page),
        "order_by": order_by,
    }
    if color:
        params["color"] = color
    url = f"{API_BASE}/search/photos?{urllib.parse.urlencode(params)}"
    body, headers = _request(url, key=key)
    return body.get("results", []) if isinstance(body, dict) else [], headers


def fetch_user_photos(username: str, *, orientation: str, order_by: str,
                      scan_pages: int, key: str) -> tuple[list[dict], dict, int]:
    """Page through GET /users/<username>/photos.

    Returns (all_photos, last_response_headers, pages_actually_fetched).
    The user endpoint doesn't support a query string — callers must filter
    client-side via filter_by_query().
    """
    all_photos: list[dict] = []
    headers: dict = {}
    fetched = 0
    for page in range(1, scan_pages + 1):
        params = {
            "per_page": "30",
            "page": str(page),
            "orientation": orientation,
            "order_by": order_by,
        }
        url = f"{API_BASE}/users/{username}/photos?{urllib.parse.urlencode(params)}"
        body, headers = _request(url, key=key)
        fetched = page
        page_photos = body if isinstance(body, list) else []
        if not page_photos:
            break
        all_photos.extend(page_photos)
        if len(page_photos) < 30:
            break  # last page reached
    return all_photos, headers, fetched


def filter_by_query(photos: list[dict], query: str) -> list[dict]:
    """Client-side filter: keep photos whose description/alt_description matches
    ANY whitespace-split term from `query` (case-insensitive, word-boundary).
    Empty query keeps everything."""
    q = query.strip()
    if not q:
        return list(photos)
    terms = [re.escape(t) for t in q.split()]
    pattern = re.compile(r"\b(" + "|".join(terms) + r")\b", re.I)
    out = []
    for p in photos:
        blob = " ".join(filter(None, [p.get("description"), p.get("alt_description")]))
        if pattern.search(blob):
            out.append(p)
    return out


def trim_candidate(p: dict) -> dict:
    """Keep only fields preview/download need. Preserves ixid in URLs."""
    return {
        "id": p["id"],
        "description": p.get("description") or p.get("alt_description") or "",
        "width": p["width"],
        "height": p["height"],
        "color": p.get("color"),
        "urls": {
            "raw": p["urls"]["raw"],
            "full": p["urls"]["full"],
            "regular": p["urls"]["regular"],
            "small": p["urls"]["small"],
            "thumb": p["urls"]["thumb"],
        },
        "links": {
            "html": p["links"]["html"],
            "download_location": p["links"]["download_location"],
        },
        "user": {
            "username": p["user"]["username"],
            "name": p["user"]["name"],
            "html": p["user"]["links"]["html"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Unsplash for retro landscape candidates.")
    parser.add_argument("query", nargs="?", default="", help="Search terms (combined with the retro/vintage seed; in --user mode this becomes a client-side keyword filter on photo descriptions).")
    parser.add_argument("--orientation", default=DEFAULT_ORIENTATION,
                        choices=["landscape", "portrait", "squarish"])
    parser.add_argument("--color", default=None,
                        choices=[None, "black_and_white", "black", "white", "yellow", "orange",
                                 "red", "purple", "magenta", "green", "teal", "blue"])
    parser.add_argument("--content-filter", default=DEFAULT_CONTENT_FILTER, choices=["low", "high"])
    parser.add_argument("--per-page", type=int, default=DEFAULT_PER_PAGE,
                        help="Cap on candidates written to _candidates.json (default 6; max 30).")
    parser.add_argument("--page", type=int, default=1,
                        help="Search-mode page number. Ignored in --user mode (use --scan-pages).")
    parser.add_argument("--order-by", default=None,
                        choices=["relevant", "latest", "oldest", "popular", "views", "downloads"],
                        help="Default 'relevant' in search mode, 'popular' in --user mode. "
                             "'relevant' only works in search mode; 'oldest'/'popular'/'views'/'downloads' only in --user mode.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help="Where _candidates.json (and later downloads) will live.")
    parser.add_argument("--no-seed", action="store_true",
                        help="Don't append the default 'retro vintage' seed to the query. "
                             "Implied in --user mode (the query is a filter, not search terms).")
    parser.add_argument("--user", default=None, metavar="USERNAME",
                        help="Limit results to one Unsplash user's uploads (e.g. 'smithsonian'). "
                             "Uses /users/<username>/photos and client-side filters the query "
                             "against photo descriptions. Useful for institutional accounts "
                             "(libraryofcongress, smithsonian, bostonpubliclibrary, etc.) whose "
                             "content gets buried in the popularity-ranked global search.")
    parser.add_argument("--scan-pages", type=int, default=3, metavar="N",
                        help="In --user mode: how many pages of 30 photos to fetch before "
                             "client-side filtering. Default 3 = 90 photos = 3 API calls. "
                             "Increase if the keyword is rare in that account's catalog.")
    args = parser.parse_args()

    key, _app = require_env()
    user_query = args.query.strip()

    if args.user:
        return _run_user_mode(args, user_query, key)
    return _run_search_mode(args, user_query, key)


def _run_search_mode(args: argparse.Namespace, user_query: str, key: str) -> int:
    order_by = args.order_by or "relevant"
    if order_by not in ("relevant", "latest"):
        die(f"--order-by {order_by!r} is only valid with --user. In search mode use 'relevant' or 'latest'.")

    if args.no_seed:
        full_query = user_query or DEFAULT_SEED
    elif user_query:
        full_query = f"{user_query} {DEFAULT_SEED}"
    else:
        full_query = DEFAULT_SEED

    results, headers = search(
        full_query,
        orientation=args.orientation,
        color=args.color,
        content_filter=args.content_filter,
        per_page=min(args.per_page, 30),
        page=args.page,
        order_by=order_by,
        key=key,
    )

    candidates = [trim_candidate(p) for p in results]
    out_dir = _write_candidates(args.output_dir, candidates, {
        "mode": "search",
        "query": full_query,
        "orientation": args.orientation,
        "color": args.color,
        "content_filter": args.content_filter,
        "page": args.page,
        "order_by": order_by,
    })

    print(f"query: {full_query!r}  orientation={args.orientation}  results={len(candidates)}")
    print(f"wrote: {out_dir / CANDIDATES_FILENAME}")
    _print_rate(headers)
    print()
    print("Next: run preview.py to render a contact sheet + terminal list.")
    return 0


def _run_user_mode(args: argparse.Namespace, user_query: str, key: str) -> int:
    order_by = args.order_by or "popular"
    if order_by == "relevant":
        die("--order-by relevant is for search mode only. In --user mode use "
            "popular (default), latest, oldest, views, or downloads.")
    if args.scan_pages < 1:
        die("--scan-pages must be >= 1")

    photos, headers, pages_fetched = fetch_user_photos(
        args.user,
        orientation=args.orientation,
        order_by=order_by,
        scan_pages=args.scan_pages,
        key=key,
    )
    matched = filter_by_query(photos, user_query)
    capped = matched[:min(args.per_page, 30)] if args.per_page else matched
    candidates = [trim_candidate(p) for p in capped]

    display_query = f"@{args.user}: {user_query}" if user_query else f"@{args.user} (no filter)"
    out_dir = _write_candidates(args.output_dir, candidates, {
        "mode": "user",
        "query": display_query,           # for preview.py display
        "user": args.user,
        "filter_query": user_query,
        "orientation": args.orientation,
        "order_by": order_by,
        "scanned_photos": len(photos),
        "scanned_pages": pages_fetched,
        "matched_before_cap": len(matched),
    })

    print(f"mode: --user @{args.user}  orientation={args.orientation}  order_by={order_by}")
    print(f"scanned: {len(photos)} photos across {pages_fetched} page(s)")
    if user_query:
        print(f"filter: matches ANY of {user_query.split()!r} (case-insensitive, word boundary)")
        print(f"matched: {len(matched)} (capped to {len(candidates)})")
    else:
        print(f"no filter query — keeping first {len(candidates)} photos")
    print(f"wrote: {out_dir / CANDIDATES_FILENAME}")
    _print_rate(headers)
    if user_query and len(matched) == 0 and pages_fetched == args.scan_pages and len(photos) == pages_fetched * 30:
        print()
        print(f"  hint: zero matches in first {len(photos)} photos. "
              f"Try --scan-pages {args.scan_pages * 2} to scan deeper, or broaden the query.")
    print()
    print("Next: run preview.py to render a contact sheet + terminal list.")
    return 0


def _write_candidates(output_dir: str, candidates: list[dict], meta: dict) -> Path:
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {**meta, "candidates": candidates}
    (out_dir / CANDIDATES_FILENAME).write_text(json.dumps(payload, indent=2))
    return out_dir


def _print_rate(headers: dict) -> None:
    remaining = headers.get("X-Ratelimit-Remaining") or headers.get("x-ratelimit-remaining")
    if remaining is None:
        return
    try:
        n = int(remaining)
        warn = "  ⚠ rate limit low" if n < 10 else ""
        print(f"rate limit remaining: {n}{warn}")
    except ValueError:
        print(f"rate limit remaining: {remaining}")


if __name__ == "__main__":
    sys.exit(main())
