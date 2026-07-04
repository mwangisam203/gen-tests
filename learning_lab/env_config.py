"""Environment variable practice."""

from __future__ import annotations

import os


def get_setting(name: str, default: str) -> str:
    """Read an environment variable with a default."""
    return os.environ.get(name, default)


def get_bool_setting(name: str, default: bool = False) -> bool:
    """Read a boolean-like environment variable."""
    value = os.environ.get(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}
