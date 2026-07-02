"""Web parsing examples that do not need a live request in tests."""

from __future__ import annotations

import requests
from bs4 import BeautifulSoup


def fetch_html(url: str, timeout: float = 5.0) -> str:
    """Download HTML and raise an error for bad responses."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def page_title(html: str) -> str:
    """Extract the page title from an HTML string."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.title is None:
        return ""
    return soup.title.get_text(strip=True)


def link_texts(html: str) -> list[str]:
    """Return visible text from all links in an HTML string."""
    soup = BeautifulSoup(html, "html.parser")
    return [link.get_text(strip=True) for link in soup.find_all("a") if link.get_text(strip=True)]
