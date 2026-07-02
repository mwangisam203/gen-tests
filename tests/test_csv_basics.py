import pytest

from learning_lab.csv_basics import read_score_rows, student_average


def test_read_score_rows(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("student,score\nAda,98\n", encoding="utf-8")

    assert read_score_rows(path) == [{"student": "Ada", "score": "98"}]


def test_student_average_uses_score_column(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("student,score\nAda,98\nGrace,94\n", encoding="utf-8")

    assert student_average(path) == 96


def test_student_average_rejects_empty_csv(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("student,score\n", encoding="utf-8")

    with pytest.raises(ValueError):
        student_average(path)
