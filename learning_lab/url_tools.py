"""URL parsing practice helpers."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def url_domain(url: str) -> str:
    """Return the network location for a URL."""
    return urlparse(url).netloc


def query_value(url: str, name: str) -> str | None:
    """Return the first query parameter value for a name."""
    values = parse_qs(urlparse(url).query).get(name)
    if not values:
        return None
    return values[0]
