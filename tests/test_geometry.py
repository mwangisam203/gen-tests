import pytest

from learning_lab.geometry import circle_area, rectangle_area, triangle_area


def test_rectangle_area_multiplies_width_and_height():
    assert rectangle_area(4, 5) == 20


def test_circle_area_rounds_to_two_places():
    assert circle_area(2) == 12.57


def test_circle_area_rejects_negative_radius():
    with pytest.raises(ValueError):
        circle_area(-1)


def test_triangle_area_halves_rectangle_area():
    assert triangle_area(4, 5) == 10
