import pytest

from learning_lab.phone_numbers import digits_only, format_us_phone


def test_digits_only_removes_formatting():
    assert digits_only("(606) 555-0100") == "6065550100"


def test_format_us_phone_formats_digits():
    assert format_us_phone("6065550100") == "(606) 555-0100"


def test_format_us_phone_rejects_wrong_length():
    with pytest.raises(ValueError):
        format_us_phone("555")
