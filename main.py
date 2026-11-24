#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt.

Choice: Mount Fuji (U+1F5FB).
A single, specific, iconic dream destination -- a snow-capped mountain
in Japan -- rather than a generic beach. It reads instantly as a
postcard at any size, names one particular trip, and is a fresh pick
against the usual beach / palm / plane entries. It is one Unicode
code point, so it is 1 character and 4 UTF-8 bytes.
"""

import os
import sys
from pathlib import Path

ENTRY = "\U0001F5FB"  # Mount Fuji

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    text = OUTPUT_PATH.read_text(encoding="utf-8")
    raw = OUTPUT_PATH.read_bytes()
    if raw != ENTRY.encode("utf-8"):
        print("invalid entry: file bytes do not match the chosen emoji", file=sys.stderr)
        return 1
    if len(text) != 1:
        print(f"invalid entry: {len(text)} characters, need exactly 1 emoji", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 8:
        print(f"invalid entry: {len(text)} characters, need 1-8", file=sys.stderr)
        return 1
    if text.strip() == "":
        print("invalid entry: only whitespace", file=sys.stderr)
        return 1
    if text.isalnum() or text.isascii():
        print("invalid entry: not an emoji", file=sys.stderr)
        return 1
    if text != ENTRY:
        print("invalid entry: output does not match chosen emoji", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {text!r} ({len(text)} char, {len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
