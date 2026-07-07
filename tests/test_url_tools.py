from learning_lab.url_tools import query_value, url_domain


def test_url_domain_returns_netloc():
    assert url_domain("https://example.com/path") == "example.com"


def test_query_value_returns_first_matching_value():
    assert query_value("https://example.com/search?q=python&q=tests", "q") == "python"


def test_query_value_returns_none_when_missing():
    assert query_value("https://example.com/search", "q") is None
