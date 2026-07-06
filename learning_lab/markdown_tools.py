"""Markdown formatting practice."""

from __future__ import annotations


def heading(text: str, level: int = 1) -> str:
    """Return a Markdown heading."""
    if not 1 <= level <= 6:
        raise ValueError("level must be between 1 and 6")
    return f"{'#' * level} {text}"


def bullet_list(items: list[str]) -> str:
    """Return a Markdown bullet list."""
    return "\n".join(f"- {item}" for item in items)
