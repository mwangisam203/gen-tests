from learning_lab.luhn import is_luhn_valid, luhn_total


def test_luhn_total_calculates_checksum_total():
    assert luhn_total("79927398713") == 70


def test_is_luhn_valid_detects_valid_number():
    assert is_luhn_valid("79927398713")
    assert not is_luhn_valid("79927398710")
