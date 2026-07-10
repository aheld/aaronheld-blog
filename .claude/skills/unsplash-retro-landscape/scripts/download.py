#!/usr/bin/env python3
"""Download chosen Unsplash photos + fire the required download-tracking ping.

Reads candidates from <output_dir>/_candidates.json (written by search.py),
saves the file bytes from urls.regular (or urls.full with --full), fires the
required GET <links.download_location> ping asynchronously for each kept image
(authorized with client_id, preserving the ixid query param), and appends a
compliant attribution credit to CREDITS.md + a per-image .credit.json sidecar.

Read SKILL.md and references/unsplash-compliance.md before changing this file.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import threading
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_OUTPUT_DIR = "content-workspace/_assets"
CANDIDATES_FILENAME = "_candidates.json"
CREDITS_FILENAME = "CREDITS.md"
FILENAME_PREFIX = "retro"


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
            "    export UNSPLASH_ACCESS_KEY=\"...\"\n"
            "    export UNSPLASH_APP_NAME=\"aaronheld-blog\""
        )
    return key, app  # type: ignore[return-value]


def load_candidates(output_dir: Path) -> dict:
    path = output_dir / CANDIDATES_FILENAME
    if not path.exists():
        die(f"no {path} — run search.py first.")
    return json.loads(path.read_text())


def fire_download_ping(download_location: str, key: str) -> None:
    """Async-safe: fire the GET, swallow errors so the user flow never blocks.

    download_location already includes the ixid query param — we keep it intact
    and add client_id as auth (Unsplash requires this or returns 401)."""
    sep = "&" if "?" in download_location else "?"
    url = f"{download_location}{sep}client_id={key}"
    req = urllib.request.Request(url, headers={"Accept-Version": "v1"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            resp.read()
    except Exception as e:
        print(f"  ⚠ download-tracking ping failed (non-fatal): {e}", file=sys.stderr)


def fetch_bytes(url: str) -> tuple[bytes, str]:
    """Fetch image bytes from images.unsplash.com. Doesn't count against rate limit."""
    req = urllib.request.Request(url, headers={"User-Agent": "unsplash-retro-landscape/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read(), resp.headers.get("Content-Type", "image/jpeg")


def write_credit(candidate: dict, app_name: str, out_dir: Path, filename: str) -> tuple[str, str]:
    """Returns (markdown_line, html_line) and writes the sidecar credit json."""
    u = candidate["user"]
    profile = f"https://unsplash.com/@{u['username']}?utm_source={app_name}&utm_medium=referral"
    unsplash = f"https://unsplash.com/?utm_source={app_name}&utm_medium=referral"

    html = (f'Photo by <a href="{profile}">{u["name"]}</a> '
            f'on <a href="{unsplash}">Unsplash</a>')
    md = f"Photo by [{u['name']}]({profile}) on [Unsplash]({unsplash})"

    sidecar = out_dir / f"{Path(filename).stem}.credit.json"
    sidecar.write_text(json.dumps({
        "photo_id": candidate["id"],
        "filename": filename,
        "unsplash_url": candidate["links"]["html"],
        "description": candidate["description"],
        "photographer": {
            "name": u["name"],
            "username": u["username"],
            "profile_url": u["html"],
        },
        "credit_markdown": md,
        "credit_html": html,
    }, indent=2))
    return md, html


def append_credits_md(out_dir: Path, entries: list[tuple[str, dict, str, str]]) -> Path:
    """entries: list of (filename, candidate, md_line, html_line)."""
    path = out_dir / CREDITS_FILENAME
    new_file = not path.exists()
    with path.open("a") as f:
        if new_file:
            f.write("# Image credits\n\n")
            f.write("Required attribution for Unsplash images saved in this directory. "
                    "Paste the Markdown line into the post; the HTML form is in each "
                    "`<filename>.credit.json` sidecar.\n\n")
        for filename, c, md, _html in entries:
            f.write(f"## `{filename}`\n\n")
            f.write(f"- **Source:** <{c['links']['html']}>\n")
            f.write(f"- **Photo ID:** `{c['id']}`\n")
            if c["description"]:
                f.write(f"- **Description:** {c['description']}\n")
            f.write(f"- **Credit (Markdown):** {md}\n\n")
    return path


def resolve_picks(payload: dict, args: argparse.Namespace) -> list[dict]:
    """Resolve picks (positional numbers + --id flags) into candidate dicts."""
    candidates = payload["candidates"]
    by_id = {c["id"]: c for c in candidates}
    chosen: list[dict] = []
    seen: set[str] = set()

    for n in args.numbers:
        if not (1 <= n <= len(candidates)):
            die(f"#{n} is out of range — only {len(candidates)} candidates.")
        c = candidates[n - 1]
        if c["id"] not in seen:
            chosen.append(c)
            seen.add(c["id"])

    for pid in args.id or []:
        if pid not in by_id:
            die(f"id {pid!r} is not in the current _candidates.json (re-run search?).")
        if pid not in seen:
            chosen.append(by_id[pid])
            seen.add(pid)

    if not chosen:
        die("no picks specified. Pass numbers (e.g. `download.py 2 5`) or `--id <photo_id>`.")
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser(description="Download chosen Unsplash candidates.")
    parser.add_argument("numbers", nargs="*", type=int,
                        help="1-indexed candidate numbers from the preview list.")
    parser.add_argument("--id", action="append", default=[],
                        help="Pick by photo id (may be repeated). Useful for cross-search picks.")
    parser.add_argument("--full", action="store_true",
                        help="Save urls.full (max dimensions) instead of urls.regular (~1080w). For hero images.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--name-prefix", default=FILENAME_PREFIX,
                        help=f"Filename prefix (default: {FILENAME_PREFIX}).")
    args = parser.parse_args()

    key, app_name = require_env()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = load_candidates(out_dir)
    chosen = resolve_picks(payload, args)

    size_key = "full" if args.full else "regular"
    print(f"Downloading {len(chosen)} image(s) at size={size_key} to {out_dir}/")

    # Fire all tracking pings in parallel daemons; join with a short grace period at the end.
    ping_threads: list[threading.Thread] = []
    credit_entries: list[tuple[str, dict, str, str]] = []

    for c in chosen:
        filename = f"{args.name_prefix}-{c['id']}.jpg"
        target = out_dir / filename

        # Async tracking ping — required by Unsplash, must not block.
        t = threading.Thread(
            target=fire_download_ping,
            args=(c["links"]["download_location"], key),
            daemon=False,
        )
        t.start()
        ping_threads.append(t)

        # Synchronous byte fetch from images.unsplash.com (doesn't count against rate limit).
        try:
            data, _ctype = fetch_bytes(c["urls"][size_key])
        except urllib.error.HTTPError as e:
            print(f"  ✗ {filename}: HTTP {e.code}")
            continue
        except Exception as e:
            print(f"  ✗ {filename}: {e}")
            continue

        target.write_bytes(data)
        md, html = write_credit(c, app_name, out_dir, filename)
        credit_entries.append((filename, c, md, html))
        kb = len(data) // 1024
        print(f"  ✓ {filename}  ({kb} KB)")

    if credit_entries:
        credits_path = append_credits_md(out_dir, credit_entries)
        print(f"\ncredits: {credits_path}")
        print("\nMarkdown credit line(s) to paste into your post:\n")
        for filename, _c, md, _html in credit_entries:
            print(f"  {filename}:")
            print(f"    {md}")

    # Give tracking pings up to 10s total to land — we don't want to silently drop them.
    for t in ping_threads:
        t.join(timeout=10)

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
