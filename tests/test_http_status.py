from learning_lab.http_status import is_success, status_family


def test_status_family_names_common_ranges():
    assert status_family(200) == "success"
    assert status_family(302) == "redirect"
    assert status_family(404) == "client error"
    assert status_family(503) == "server error"


def test_status_family_handles_unknown_codes():
    assert status_family(42) == "unknown"


def test_is_success_detects_2xx_codes():
    assert is_success(204)
    assert not is_success(404)
