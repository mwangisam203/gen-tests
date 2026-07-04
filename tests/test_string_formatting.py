import pytest

from learning_lab.string_formatting import progress_label, receipt_line


def test_receipt_line_aligns_name_and_price():
    assert receipt_line("Pen", 1.5) == "Pen          $  1.50"


def test_progress_label_formats_percent():
    assert progress_label(3, 4) == "3/4 complete (75%)"


def test_progress_label_rejects_non_positive_total():
    with pytest.raises(ValueError):
        progress_label(1, 0)
