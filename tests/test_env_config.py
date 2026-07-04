from learning_lab.env_config import get_bool_setting, get_setting


def test_get_setting_returns_default_when_missing(monkeypatch):
    monkeypatch.delenv("LESSON_MODE", raising=False)

    assert get_setting("LESSON_MODE", "practice") == "practice"


def test_get_setting_reads_environment(monkeypatch):
    monkeypatch.setenv("LESSON_MODE", "review")

    assert get_setting("LESSON_MODE", "practice") == "review"


def test_get_bool_setting_understands_true_words(monkeypatch):
    monkeypatch.setenv("FEATURE_ON", "yes")

    assert get_bool_setting("FEATURE_ON")
