"""Tokenization practice helpers."""

from __future__ import annotations

import re


def words(text: str) -> list[str]:
    """Return lowercase word tokens."""
    return re.findall(r"[a-z0-9]+", text.lower())


def bigrams(text: str) -> list[tuple[str, str]]:
    """Return neighboring word pairs."""
    tokens = words(text)
    return list(zip(tokens, tokens[1:]))
