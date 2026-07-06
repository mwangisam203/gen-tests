import pytest

from learning_lab.markdown_tools import bullet_list, heading


def test_heading_uses_requested_level():
    assert heading("Practice", level=2) == "## Practice"


def test_heading_rejects_invalid_level():
    with pytest.raises(ValueError):
        heading("Practice", level=7)


def test_bullet_list_formats_items():
    assert bullet_list(["read", "test"]) == "- read\n- test"
