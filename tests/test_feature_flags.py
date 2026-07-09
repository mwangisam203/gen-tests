from learning_lab.feature_flags import disable, enable, is_enabled


def test_is_enabled_defaults_to_false():
    assert not is_enabled({}, "new_ui")


def test_enable_turns_flag_on_without_mutating_original():
    flags = {}

    assert enable(flags, "new_ui") == {"new_ui": True}
    assert flags == {}


def test_disable_turns_flag_off():
    assert disable({"new_ui": True}, "new_ui") == {"new_ui": False}
