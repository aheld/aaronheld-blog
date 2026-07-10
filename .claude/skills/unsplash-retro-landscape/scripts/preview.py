#!/usr/bin/env python3
"""Render candidate previews from _candidates.json.

Writes <output_dir>/preview.html (hotlinked contact sheet, ixid preserved on
every image) and prints a numbered terminal list. If the terminal supports
inline images (iTerm2, kitty, or `chafa` on PATH), renders small thumbnails
inline as well.

Crucially: this script does NOT fire download-tracking events. Hotlinking
previews from images.unsplash.com already counts as a view, and image
requests don't count against the API rate limit. Read
references/unsplash-compliance.md before changing this file.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

DEFAULT_OUTPUT_DIR = "content-workspace/_assets"
CANDIDATES_FILENAME = "_candidates.json"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def load_candidates(output_dir: Path) -> dict:
    path = output_dir / CANDIDATES_FILENAME
    if not path.exists():
        die(f"no {path} — run search.py first.")
    return json.loads(path.read_text())


def render_html(payload: dict, app_name: str) -> str:
    cards = []
    for i, c in enumerate(payload["candidates"], 1):
        credit_html = (
            f'Photo by <a href="https://unsplash.com/@{c["user"]["username"]}'
            f'?utm_source={app_name}&utm_medium=referral">{c["user"]["name"]}</a> '
            f'on <a href="https://unsplash.com/?utm_source={app_name}&utm_medium=referral">Unsplash</a>'
        )
        cards.append(f'''
<figure class="card">
  <div class="num">#{i}</div>
  <a href="{c["links"]["html"]}" target="_blank" rel="noopener">
    <img src="{c["urls"]["small"]}" alt="{(c["description"] or "Unsplash photo").replace('"', "&quot;")}" loading="lazy">
  </a>
  <figcaption>
    <div class="desc">{c["description"] or "<em>(no description)</em>"}</div>
    <div class="meta">{c["width"]}×{c["height"]} · <code>{c["id"]}</code></div>
    <div class="credit">{credit_html}</div>
  </figcaption>
</figure>''')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Unsplash candidates — {payload["query"]}</title>
<style>
  body {{ font-family: -apple-system, system-ui, sans-serif; margin: 1.5rem; background: #111; color: #eee; }}
  h1 {{ font-size: 1.1rem; font-weight: 500; color: #aaa; margin-bottom: 1rem; }}
  h1 code {{ color: #ffd479; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1rem; }}
  .card {{ background: #1a1a1a; border-radius: 8px; overflow: hidden; margin: 0; position: relative; }}
  .card img {{ width: 100%; height: 220px; object-fit: cover; display: block; }}
  .num {{ position: absolute; top: 8px; left: 8px; background: rgba(0,0,0,.7); color: #ffd479; padding: 2px 8px; border-radius: 4px; font-weight: 600; }}
  figcaption {{ padding: .75rem; font-size: .85rem; }}
  .desc {{ margin-bottom: .4rem; color: #ddd; }}
  .meta {{ color: #888; font-size: .75rem; margin-bottom: .4rem; }}
  .meta code {{ color: #aaa; }}
  .credit {{ font-size: .75rem; color: #888; }}
  .credit a {{ color: #aaa; }}
</style>
</head>
<body>
<h1>Unsplash candidates · query: <code>{payload["query"]}</code> · orientation: <code>{payload["orientation"]}</code> · {len(payload["candidates"])} results</h1>
<div class="grid">{"".join(cards)}
</div>
</body>
</html>"""


def can_inline_images() -> str | None:
    """Return 'iterm', 'kitty', 'chafa', or None."""
    if os.environ.get("TERM_PROGRAM") == "iTerm.app":
        return "iterm"
    if os.environ.get("TERM", "").startswith("xterm-kitty"):
        return "kitty"
    if shutil.which("chafa"):
        return "chafa"
    return None


def render_inline(thumb_url: str, mode: str) -> None:
    """Best-effort inline thumbnail render. Silently skips on any error."""
    try:
        with urllib.request.urlopen(thumb_url, timeout=10) as resp:
            data = resp.read()
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(data)
            tmp = f.name
        if mode == "iterm":
            import base64
            b64 = base64.b64encode(data).decode("ascii")
            sys.stdout.write(f"\033]1337;File=inline=1;height=8;preserveAspectRatio=1:{b64}\a\n")
            sys.stdout.flush()
        elif mode == "kitty":
            subprocess.run(["kitty", "+kitten", "icat", "--align=left", "--place=40x8@0x0", tmp],
                           check=False)
        elif mode == "chafa":
            subprocess.run(["chafa", "--size=40x8", tmp], check=False)
        try:
            os.unlink(tmp)
        except OSError:
            pass
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Render candidate previews (HTML + terminal).")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--no-html", action="store_true", help="Skip writing preview.html.")
    parser.add_argument("--no-inline", action="store_true",
                        help="Skip inline terminal thumbnails even if supported.")
    args = parser.parse_args()

    app_name = os.environ.get("UNSPLASH_APP_NAME", "your_app_name")

    out_dir = Path(args.output_dir)
    payload = load_candidates(out_dir)
    candidates = payload["candidates"]
    if not candidates:
        print("no candidates in _candidates.json. Try a different query.")
        return 0

    if not args.no_html:
        html_path = out_dir / "preview.html"
        html_path.write_text(render_html(payload, app_name))
        print(f"wrote: {html_path}   (open in a browser: open {html_path})")
        print()

    inline_mode = None if args.no_inline else can_inline_images()
    if inline_mode:
        print(f"(inline thumbnails: {inline_mode})\n")

    for i, c in enumerate(candidates, 1):
        desc = c["description"] or "(no description)"
        if len(desc) > 70:
            desc = desc[:67] + "…"
        print(f"#{i:>2}  {desc}")
        print(f"      {c['width']}×{c['height']}  id={c['id']}  by {c['user']['name']} (@{c['user']['username']})")
        print(f"      page: {c['links']['html']}")
        print(f"      preview URL: {c['urls']['small']}")
        if inline_mode:
            render_inline(c["urls"]["thumb"], inline_mode)
        print()

    print(f"Pick by number or id, then run:")
    print(f"  python3 .claude/skills/unsplash-retro-landscape/scripts/download.py <num> [<num> ...]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
