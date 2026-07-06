import pytest

from learning_lab.config_parser import parse_bool, parse_int_setting


def test_parse_bool_accepts_true_and_false_words():
    assert parse_bool("yes")
    assert not parse_bool("off")


def test_parse_bool_rejects_unknown_values():
    with pytest.raises(ValueError):
        parse_bool("maybe")


def test_parse_int_setting_reads_default_or_value():
    assert parse_int_setting({}, "limit", 10) == 10
    assert parse_int_setting({"limit": "5"}, "limit", 10) == 5
