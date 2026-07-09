import pytest

from learning_lab.dice_probability import probability_of_total, two_die_totals


def test_two_die_totals_counts_common_totals():
    counts = two_die_totals()

    assert counts[2] == 1
    assert counts[7] == 6


def test_two_die_totals_rejects_bad_sides():
    with pytest.raises(ValueError):
        two_die_totals(0)


def test_probability_of_total_uses_outcome_count():
    assert probability_of_total(7) == 6 / 36
