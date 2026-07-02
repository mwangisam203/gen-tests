from learning_lab.file_basics import count_non_empty_lines, read_lines, write_note


def test_write_note_and_read_lines(tmp_path):
    note_path = tmp_path / "note.md"

    write_note(note_path, "Today", "Practice a little Python.")

    assert read_lines(note_path) == ["# Today", "", "Practice a little Python."]


def test_count_non_empty_lines(tmp_path):
    path = tmp_path / "lines.txt"
    path.write_text("alpha\n\n beta \n", encoding="utf-8")

    assert count_non_empty_lines(path) == 2
