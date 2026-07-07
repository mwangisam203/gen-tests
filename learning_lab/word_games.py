"""Word game practice helpers."""

from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """Return True when text reads the same backward."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def anagram_key(word: str) -> str:
    """Return a normalized key for anagram comparisons."""
    return "".join(sorted(word.lower()))


def are_anagrams(left: str, right: str) -> bool:
    """Return True when two words contain the same letters."""
    return anagram_key(left) == anagram_key(right)
