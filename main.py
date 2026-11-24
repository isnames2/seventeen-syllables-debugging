#!/usr/bin/env python3
"""Write the debugging haiku to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

# 5-7-5 syllables: "Cursor blinks at three" (5), "a stack trace scrolls
# past midnight" (7), "the bug was one char" (5). 80 bytes total.
HAIKU = (
    "Cursor blinks at three\n"
    "a stack trace scrolls past midnight\n"
    "the bug was one char\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
