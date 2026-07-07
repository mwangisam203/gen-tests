"""Color conversion practice helpers."""

from __future__ import annotations


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Convert RGB values to a hex color."""
    for value in (red, green, blue):
        if not 0 <= value <= 255:
            raise ValueError("RGB values must be between 0 and 255")
    return f"#{red:02x}{green:02x}{blue:02x}"


def hex_to_rgb(color: str) -> tuple[int, int, int]:
    """Convert a hex color to RGB values."""
    cleaned = color.removeprefix("#")
    if len(cleaned) != 6:
        raise ValueError("hex color must have six digits")
    return int(cleaned[0:2], 16), int(cleaned[2:4], 16), int(cleaned[4:6], 16)
