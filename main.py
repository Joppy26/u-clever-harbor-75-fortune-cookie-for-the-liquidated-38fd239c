#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to entry.txt in the output directory.
"""

import os
import sys


FORTUNE = "Your luck is about to change; the market already changed it once, and kept the change."


def validate_fortune(text: str) -> str:
    """Check the fortune against the gate before writing it.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    whitespace, and the task caps the line at 20 words.
    """
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 160):
        raise ValueError(f"fortune must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(text.split()) > 20:
        raise ValueError(f"fortune must be at most 20 words, got {len(text.split())}")
    return text


def write_entry(fortune: str, out_dir: str) -> str:
    """Validate the fortune and write it as entry.txt in out_dir."""
    line = validate_fortune(fortune)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(FORTUNE, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
