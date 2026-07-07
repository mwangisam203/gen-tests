"""Email address practice helpers."""

from __future__ import annotations


def split_email(email: str) -> tuple[str, str]:
    """Split an email address into local part and domain."""
    if email.count("@") != 1:
        raise ValueError("email must contain one @")
    local, domain = email.split("@")
    if not local or not domain:
        raise ValueError("email must include local part and domain")
    return local, domain


def domain_of(email: str) -> str:
    """Return the domain part of an email address."""
    return split_email(email)[1].lower()
