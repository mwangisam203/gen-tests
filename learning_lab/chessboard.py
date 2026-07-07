"""Chessboard coordinate practice."""

from __future__ import annotations


FILES = "abcdefgh"


def square_color(square: str) -> str:
    """Return the color of a chess square."""
    file = FILES.index(square[0].lower()) + 1
    rank = int(square[1])
    return "dark" if (file + rank) % 2 == 0 else "light"


def is_valid_square(square: str) -> bool:
    """Return True for coordinates like e4."""
    return len(square) == 2 and square[0].lower() in FILES and square[1] in "12345678"
