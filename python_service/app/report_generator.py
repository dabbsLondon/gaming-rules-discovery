"""Generate simple HTML reports for harvest results."""

from typing import Iterable


def generate_report(items: Iterable[str]) -> str:
    body = "\n".join(f"<li>{item}</li>" for item in items)
    return f"<html><body><ul>{body}</ul></body></html>"
