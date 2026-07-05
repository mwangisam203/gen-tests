"""Inventory practice examples."""

from __future__ import annotations


Inventory = dict[str, int]


def add_stock(inventory: Inventory, item: str, amount: int) -> Inventory:
    """Return a copy of inventory with stock added."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    updated = inventory.copy()
    updated[item] = updated.get(item, 0) + amount
    return updated


def low_stock(inventory: Inventory, threshold: int) -> list[str]:
    """Return item names at or below the stock threshold."""
    return [item for item, count in inventory.items() if count <= threshold]


def total_units(inventory: Inventory) -> int:
    """Return all units in inventory."""
    return sum(inventory.values())


def remove_stock(inventory: Inventory, item: str, amount: int) -> Inventory:
    """Return a copy of inventory with stock removed."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if inventory.get(item, 0) < amount:
        raise ValueError("not enough stock")
    updated = inventory.copy()
    updated[item] -= amount
    return updated
