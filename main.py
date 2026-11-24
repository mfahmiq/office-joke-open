#!/usr/bin/env python3
"""Office Joke Open entry.

Writes a single line of office comedy to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies it against the gate:
UTF-8 text, 1-200 characters, a single line, not whitespace-only.
Exits non-zero on any failure. Python standard library only.
"""

import os
import sys

ENTRY = "I asked IT to fix the printer and they emailed me a 47-step guide that I had to print."


def main() -> int:
    text = ENTRY

    # Self-verification against the gate, before writing anything.
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"FAIL: entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry is whitespace-only", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)

    # Verify what was written matches the entry byte for byte.
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("FAIL: written entry.txt does not match ENTRY", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(text)}-char entry to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
