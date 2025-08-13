"""Batch harvesting CLI."""

from dataclasses import dataclass
from pathlib import Path
from typing import List
import hashlib

from . import ocr_service


@dataclass(frozen=True)
class HarvestedImage:
    """Metadata about a harvested image and its extracted text."""

    path: str
    digest: str
    text: str
    is_legion_rule: bool


def run(directory: str) -> List[HarvestedImage]:
    """Return metadata for unique images in the given directory.

    Duplicate images are identified via an MD5 hash of their contents and are
    ignored so the same rules are not processed multiple times. The digest is
    returned alongside the file path so callers can track already ingested
    rules.
    """
    path = Path(directory)
    seen_hashes = set()
    unique_files: List[HarvestedImage] = []
    supported_exts = {".jpg", ".jpeg", ".png"}
    for p in path.glob("*"):
        if not p.is_file() or p.suffix.lower() not in supported_exts:
            continue
        digest = hashlib.md5(p.read_bytes()).hexdigest()
        if digest in seen_hashes:
            continue
        text = ocr_service.extract_text(str(p))
        is_legion_rule = "legion" in text.lower()
        seen_hashes.add(digest)
        unique_files.append(HarvestedImage(str(p), digest, text, is_legion_rule))
    return unique_files


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="HH3 batch harvester")
    parser.add_argument("dir", help="Directory containing sample images")
    args = parser.parse_args()

    for img in run(args.dir):
        print(img)
