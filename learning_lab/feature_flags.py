"""Feature flag practice helpers."""

from __future__ import annotations


def is_enabled(flags: dict[str, bool], name: str) -> bool:
    """Return whether a feature flag is enabled."""
    return flags.get(name, False)


def enable(flags: dict[str, bool], name: str) -> dict[str, bool]:
    """Return a copy with a feature enabled."""
    updated = flags.copy()
    updated[name] = True
    return updated


def disable(flags: dict[str, bool], name: str) -> dict[str, bool]:
    """Return a copy with a feature disabled."""
    updated = flags.copy()
    updated[name] = False
    return updated
