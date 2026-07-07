import pytest

from learning_lab.retry_tools import retry


def test_retry_returns_successful_result_after_failure():
    calls = {"count": 0}

    def sometimes():
        calls["count"] += 1
        if calls["count"] == 1:
            raise RuntimeError("try again")
        return "ok"

    assert retry(sometimes, attempts=2) == "ok"


def test_retry_rejects_bad_attempt_count():
    with pytest.raises(ValueError):
        retry(lambda: "ok", attempts=0)
