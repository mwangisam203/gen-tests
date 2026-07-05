import pytest

from learning_lab.errors import divide, parse_int, require_key, safe_get


def test_divide_rejects_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_parse_int_returns_default_for_bad_input():
    assert parse_int("nope", default=0) == 0


def test_parse_int_reraises_without_default():
    with pytest.raises(ValueError):
        parse_int("nope")


def test_require_key_returns_value_or_raises():
    assert require_key({"name": "Ada"}, "name") == "Ada"
    with pytest.raises(KeyError):
        require_key({}, "name")


def test_safe_get_returns_default_when_key_is_missing():
    assert safe_get({"name": "Ada"}, "name") == "Ada"
    assert safe_get({}, "name", default="Unknown") == "Unknown"
