"""String formatting practice."""

from __future__ import annotations


def receipt_line(name: str, price: float) -> str:
    """Format a receipt line."""
    return f"{name:<12} ${price:>6.2f}"


def progress_label(done: int, total: int) -> str:
    """Format completion progress."""
    if total <= 0:
        raise ValueError("total must be positive")
    percent = done / total * 100
    return f"{done}/{total} complete ({percent:.0f}%)"
