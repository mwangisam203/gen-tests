"""State machine practice helpers."""

from __future__ import annotations


TRANSITIONS = {
    "draft": {"submit": "review"},
    "review": {"approve": "published", "reject": "draft"},
    "published": {},
}


def next_state(state: str, action: str) -> str:
    """Return the next state for an action."""
    try:
        return TRANSITIONS[state][action]
    except KeyError as error:
        raise ValueError(f"invalid transition: {state} -> {action}") from error


def available_actions(state: str) -> list[str]:
    """Return actions available for a state."""
    return sorted(TRANSITIONS.get(state, {}))
