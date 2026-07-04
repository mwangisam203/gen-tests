import random

import pytest

from learning_lab.random_tools import coin_flip, roll_die


def test_coin_flip_uses_given_rng():
    rng = random.Random(1)

    assert coin_flip(rng) == "heads"


def test_roll_die_returns_value_in_range():
    rng = random.Random(1)

    assert 1 <= roll_die(6, rng) <= 6


def test_roll_die_rejects_too_few_sides():
    with pytest.raises(ValueError):
        roll_die(1)
