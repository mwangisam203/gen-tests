import pytest

from learning_lab.cli import main, run_lesson


def test_run_lesson_numbers():
    assert "$25.00 with tax is $26.50" in run_lesson("numbers")


def test_run_lesson_text():
    assert run_lesson("text") == "Slug: learning-python-one-step-at-a-time"


def test_run_lesson_rejects_unknown_lesson():
    with pytest.raises(ValueError):
        run_lesson("unknown")


def test_main_prints_lesson(capsys):
    assert main(["text"]) == 0

    captured = capsys.readouterr()
    assert "learning-python-one-step-at-a-time" in captured.out
