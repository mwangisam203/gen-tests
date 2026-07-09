import pytest

from learning_lab.binary_tools import binary_to_int, int_to_binary


def test_int_to_binary_formats_digits():
    assert int_to_binary(10) == "1010"


def test_int_to_binary_rejects_negative_numbers():
    with pytest.raises(ValueError):
        int_to_binary(-1)


def test_binary_to_int_parses_bits():
    assert binary_to_int("1010") == 10


def test_binary_to_int_rejects_bad_bits():
    with pytest.raises(ValueError):
        binary_to_int("102")
