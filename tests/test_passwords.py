from learning_lab.passwords import has_digit, has_uppercase, password_strength


def test_has_digit_detects_digits():
    assert has_digit("abc1")
    assert not has_digit("abc")


def test_has_uppercase_detects_uppercase_letters():
    assert has_uppercase("Ada")
    assert not has_uppercase("ada")


def test_password_strength_scores_rules():
    assert password_strength("Short1") == "medium"
    assert password_strength("longbutplain") == "weak"
    assert password_strength("Learning1") == "strong"
