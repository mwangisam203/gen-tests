from learning_lab.context_managers import temporary_value


def test_temporary_value_restores_existing_value():
    data = {"mode": "practice"}

    with temporary_value(data, "mode", "test"):
        assert data["mode"] == "test"

    assert data["mode"] == "practice"


def test_temporary_value_removes_new_key_afterward():
    data = {}

    with temporary_value(data, "mode", "test"):
        assert data["mode"] == "test"

    assert data == {}
