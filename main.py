#!/usr/bin/env python3
"""Weirdest Job Title - make.fun blind-judge entry (stdlib only).

Writes the single-line entry (<=60 chars) to /output/entry.txt.
"""
import os

TITLE = "CEO of the Department of Lost Remote Controls"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear contents only; never delete the /output folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE + "\n")


if __name__ == "__main__":
    main()
