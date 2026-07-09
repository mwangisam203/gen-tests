"""Input sanitizer practice helpers."""

from __future__ import annotations

import html


def collapse_spaces(text: str) -> str:
    """Collapse repeated whitespace to single spaces."""
    return " ".join(text.split())


def escape_html(text: str) -> str:
    """Escape text for safe HTML display."""
    return html.escape(text, quote=True)
