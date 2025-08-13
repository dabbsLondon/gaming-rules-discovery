"""Batch harvesting CLI."""

from pathlib import Path
from typing import List


def run(directory: str) -> List[str]:
    """Return a list of image files in the given directory."""
    path = Path(directory)
    return [str(p) for p in path.glob("*") if p.is_file()]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="HH3 batch harvester")
    parser.add_argument("dir", help="Directory containing sample images")
    args = parser.parse_args()

    for img in run(args.dir):
        print(img)
