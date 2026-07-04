"""Randomness practice examples."""

from __future__ import annotations

import random


def coin_flip(rng: random.Random | None = None) -> str:
    """Return heads or tails."""
    generator = rng or random.Random()
    return generator.choice(["heads", "tails"])


def roll_die(sides: int = 6, rng: random.Random | None = None) -> int:
    """Roll a die with the given number of sides."""
    if sides < 2:
        raise ValueError("sides must be at least 2")
    generator = rng or random.Random()
    return generator.randint(1, sides)
