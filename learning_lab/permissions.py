"""Permission practice helpers."""

from __future__ import annotations


def can_edit(role: str) -> bool:
    """Return True when a role can edit."""
    return role in {"admin", "editor"}


def can_delete(role: str, owns_item: bool) -> bool:
    """Return True when a user can delete an item."""
    return role == "admin" or owns_item


def allowed_actions(role: str, owns_item: bool = False) -> list[str]:
    """Return actions available to a role."""
    actions = ["view"]
    if can_edit(role):
        actions.append("edit")
    if can_delete(role, owns_item):
        actions.append("delete")
    return actions
