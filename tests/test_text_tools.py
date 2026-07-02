from learning_lab.text_tools import initials, normalize_name, slugify


def test_normalize_name_trims_and_cases():
    assert normalize_name("  ada   lovelace ") == "Ada Lovelace"


def test_slugify_removes_punctuation():
    assert slugify("Python Tests: A Tiny Guide!") == "python-tests-a-tiny-guide"


def test_initials_uses_each_name_part():
    assert initials("grace brewster hopper") == "GBH"
