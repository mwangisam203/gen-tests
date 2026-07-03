"""A tiny shopping cart example."""

from __future__ import annotations


CartItem = dict[str, float | str | int]


def line_total(item: CartItem) -> float:
    """Return quantity times price for one cart item."""
    return round(float(item["price"]) * int(item["quantity"]), 2)


def cart_total(items: list[CartItem]) -> float:
    """Return the total for all cart items."""
    return round(sum(line_total(item) for item in items), 2)


def item_names(items: list[CartItem]) -> list[str]:
    """Return cart item names in order."""
    return [str(item["name"]) for item in items]
