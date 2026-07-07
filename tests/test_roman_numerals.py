import pytest

from learning_lab.roman_numerals import to_roman


def test_to_roman_uses_subtractive_notation():
    assert to_roman(4) == "IV"
    assert to_roman(944) == "CMXLIV"


def test_to_roman_rejects_out_of_range_numbers():
    with pytest.raises(ValueError):
        to_roman(0)
