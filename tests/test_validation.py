import pytest

from learning_lab.validation import require_between, require_non_empty


def test_require_non_empty_strips_text():
    assert require_non_empty(" Ada ", "name") == "Ada"


def test_require_non_empty_rejects_blank_text():
    with pytest.raises(ValueError):
        require_non_empty("   ", "name")


def test_require_between_accepts_inclusive_range():
    assert require_between(5, 1, 5) == 5


def test_require_between_rejects_outside_range():
    with pytest.raises(ValueError):
        require_between(6, 1, 5)
