from learning_lab.path_tools import ensure_folder, file_extension, sibling_path


def test_file_extension_omits_dot():
    assert file_extension("notes.md") == "md"


def test_sibling_path_uses_same_parent():
    assert sibling_path("docs/notes.md", "plan.md").as_posix() == "docs/plan.md"


def test_ensure_folder_creates_directory(tmp_path):
    folder = ensure_folder(tmp_path / "nested" / "folder")

    assert folder.is_dir()
