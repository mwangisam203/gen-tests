from learning_lab.checksum_tools import digit_sum, mod10_check_digit


def test_digit_sum_ignores_non_digits():
    assert digit_sum("A12-B3") == 6


def test_mod10_check_digit_completes_next_ten():
    assert mod10_check_digit("123") == 4
    assert mod10_check_digit("55") == 0
