#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: one original dad joke, one line.

The joke was chosen by a two-way pairwise arena against 16 candidates
and against the lane's gold-set winners (see ARENA.md). It is a dad joke
a dad would tell out loud: a clock goes in a blender, and the punchline
"in no time" lands two ways at once — fast, and with no clock left.

Writes exactly these bytes to /output/entry.txt (no trailing newline),
deterministically, so two runs agree byte for byte. Stdlib only.
MAKEFUN_OUTPUT_DIR stands in for /output outside the grader's container.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I put a clock in the blender; now I make smoothies in no time."


def main():
    # Gate enforced here as well as by the sealed scorer: 1-140 chars.
    if not 1 <= len(JOKE) <= 140 or not JOKE.strip():
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-140")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
