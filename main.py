#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes a single line, at most 200 characters, about a small good thing
that happened today, to /output/entry.txt and nothing else.
Standard library only; no network access.
"""

import os

LINE = (
    "The warung auntie slipped a still-warm gorengan into my bag for free, "
    "winked, and said the rain had already paid for it."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written.decode("utf-8") != LINE:
        raise ValueError("written file does not round-trip to the line")
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
