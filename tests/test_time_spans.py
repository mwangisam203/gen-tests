import pytest

from learning_lab.time_spans import format_duration, minutes_to_hours


def test_minutes_to_hours_returns_hours_and_leftover_minutes():
    assert minutes_to_hours(135) == (2, 15)


def test_minutes_to_hours_rejects_negative_minutes():
    with pytest.raises(ValueError):
        minutes_to_hours(-1)


def test_format_duration_uses_two_digit_fields():
    assert format_duration(75) == "01:15"
