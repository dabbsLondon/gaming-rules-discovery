"""Text embedding utilities."""

from typing import List


def embed_text(text: str) -> List[float]:
    """Return a dummy embedding vector for the given text."""
    return [0.0 for _ in text.split()]
