import pytest

from learning_lab.state_machine import available_actions, next_state


def test_next_state_applies_valid_transition():
    assert next_state("draft", "submit") == "review"


def test_next_state_rejects_invalid_transition():
    with pytest.raises(ValueError):
        next_state("published", "submit")


def test_available_actions_lists_state_actions():
    assert available_actions("review") == ["approve", "reject"]
