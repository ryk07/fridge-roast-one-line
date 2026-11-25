#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast of a smart fridge (<= 200 chars) to
/output/entry.txt. Stdlib only; paths resolved from __file__.
"""

import os

ROAST = (
    "My smart fridge pushed a firmware update at 3 a.m. \u2014 "
    "now the ice maker won't work until I accept the terms, "
    "and the milk expired while I was still scrolling."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
