import pytest

from learning_lab.color_tools import hex_to_rgb, rgb_to_hex


def test_rgb_to_hex_formats_lowercase_hex():
    assert rgb_to_hex(255, 165, 0) == "#ffa500"


def test_rgb_to_hex_rejects_out_of_range_values():
    with pytest.raises(ValueError):
        rgb_to_hex(256, 0, 0)


def test_hex_to_rgb_parses_color():
    assert hex_to_rgb("#ffa500") == (255, 165, 0)
