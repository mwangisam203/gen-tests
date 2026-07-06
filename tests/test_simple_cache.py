from learning_lab.simple_cache import get_or_remember, remember


def test_remember_stores_value():
    cache = {}

    assert remember(cache, "mode", "practice") == "practice"
    assert cache == {"mode": "practice"}


def test_get_or_remember_keeps_existing_value():
    cache = {"mode": "review"}

    assert get_or_remember(cache, "mode", "practice") == "review"
    assert cache == {"mode": "review"}


def test_get_or_remember_stores_missing_value():
    cache = {}

    assert get_or_remember(cache, "mode", "practice") == "practice"
    assert cache == {"mode": "practice"}
