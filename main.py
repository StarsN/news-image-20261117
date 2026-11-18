#!/usr/bin/env python3
"""news-image-20261117 entry: copy the bundled front-page image to the output.

The image (entry.png, beside this file) is a one-page newspaper front page
summing up the world news of Tuesday 17 November 2026: the U.S.-Iran strikes
in the Gulf, the Kerch Bridge hit again, tumbling markets, a cyberattack on
178 top websites, and more.

The program uses only the standard library, does no network access, and
writes the same bytes on every run: it copies entry.png byte for byte.

Run locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

In the grader the output directory is /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
