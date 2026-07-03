"""HTTP status code examples."""

from __future__ import annotations


def status_family(status_code: int) -> str:
    """Return the common family name for an HTTP status code."""
    if 100 <= status_code <= 199:
        return "informational"
    if 200 <= status_code <= 299:
        return "success"
    if 300 <= status_code <= 399:
        return "redirect"
    if 400 <= status_code <= 499:
        return "client error"
    if 500 <= status_code <= 599:
        return "server error"
    return "unknown"


def is_success(status_code: int) -> bool:
    """Return True for 2xx status codes."""
    return status_family(status_code) == "success"
