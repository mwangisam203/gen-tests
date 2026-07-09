from learning_lab.isbn_tools import is_valid_isbn10, normalize_isbn10


def test_normalize_isbn10_removes_separators():
    assert normalize_isbn10("0-306-40615-2") == "0306406152"


def test_is_valid_isbn10_checks_checksum():
    assert is_valid_isbn10("0-306-40615-2")
    assert not is_valid_isbn10("0-306-40615-3")
