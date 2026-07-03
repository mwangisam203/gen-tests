import pytest

from learning_lab.json_basics import profile_summary, read_json


def test_read_json_returns_object(tmp_path):
    path = tmp_path / "profile.json"
    path.write_text('{"name": "Ada"}', encoding="utf-8")

    assert read_json(path) == {"name": "Ada"}


def test_read_json_rejects_non_object_roots(tmp_path):
    path = tmp_path / "items.json"
    path.write_text("[1, 2, 3]", encoding="utf-8")

    with pytest.raises(ValueError):
        read_json(path)


def test_profile_summary_uses_defaults():
    assert profile_summary({"name": "Grace"}) == "Grace is practicing Python."
