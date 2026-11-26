#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene - entry writer.

Writes the one family scene to /output/entry.txt.
Deterministic: fixed text, no randomness, no network, no input besides
this file. Run with: python3 main.py
"""

import os

ENTRY = (
    "My six-year-old taught Grandma to video-call tonight, then whispered, "
    "'I learned it from watching you help me.'\n"
    "Grandma cried, I cried, and even the Wi-Fi behaved for once \u2014 "
    "kindness, passed down like a recipe card."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
