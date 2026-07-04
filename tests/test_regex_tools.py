from learning_lab.regex_tools import find_numbers, has_zip_code, mask_email


def test_find_numbers_returns_ints():
    assert find_numbers("Room 12 has 3 chairs") == [12, 3]


def test_mask_email_hides_middle_characters():
    assert mask_email("ada@example.com") == "a*a@example.com"
    assert mask_email("al@example.com") == "a*@example.com"


def test_has_zip_code_matches_five_digits():
    assert has_zip_code("Somerset KY 42501")
    assert not has_zip_code("Room 425")
