"""Simple password validation practice."""

from __future__ import annotations


def has_digit(text: str) -> bool:
    """Return True when text contains any digit."""
    return any(char.isdigit() for char in text)


def has_uppercase(text: str) -> bool:
    """Return True when text contains any uppercase letter."""
    return any(char.isupper() for char in text)


def password_strength(password: str) -> str:
    """Return a basic password strength label."""
    score = 0
    score += len(password) >= 8
    score += has_digit(password)
    score += has_uppercase(password)
    if score == 3:
        return "strong"
    if score == 2:
        return "medium"
    return "weak"


def missing_password_rules(password: str) -> list[str]:
    """Return rule names that a password does not satisfy."""
    missing: list[str] = []
    if len(password) < 8:
        missing.append("length")
    if not has_digit(password):
        missing.append("digit")
    if not has_uppercase(password):
        missing.append("uppercase")
    return missing
