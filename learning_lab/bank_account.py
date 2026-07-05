"""Bank account practice examples."""

from __future__ import annotations


def deposit(balance: float, amount: float) -> float:
    """Return a balance after a deposit."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    return round(balance + amount, 2)


def withdraw(balance: float, amount: float) -> float:
    """Return a balance after a withdrawal."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("insufficient funds")
    return round(balance - amount, 2)


def apply_interest(balance: float, annual_rate: float) -> float:
    """Apply one year of simple interest."""
    return round(balance * (1 + annual_rate), 2)


def transfer(source_balance: float, target_balance: float, amount: float) -> tuple[float, float]:
    """Move money from one balance to another."""
    new_source = withdraw(source_balance, amount)
    new_target = deposit(target_balance, amount)
    return new_source, new_target
