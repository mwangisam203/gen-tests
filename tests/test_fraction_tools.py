from fractions import Fraction

from learning_lab.fraction_tools import add_fractions, simplify_fraction


def test_simplify_fraction_reduces_terms():
    assert simplify_fraction(4, 8) == Fraction(1, 2)


def test_add_fractions_returns_fraction_sum():
    assert add_fractions((1, 4), (1, 2)) == Fraction(3, 4)
