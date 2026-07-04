"""Set practice examples."""

from __future__ import annotations


def unique_names(names: list[str]) -> set[str]:
    """Return unique names while normalizing case."""
    return {name.strip().title() for name in names if name.strip()}


def shared_items(left: set[str], right: set[str]) -> set[str]:
    """Return items that appear in both sets."""
    return left & right


def missing_items(required: set[str], provided: set[str]) -> set[str]:
    """Return required items that were not provided."""
    return required - provided
