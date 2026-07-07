import pytest

from learning_lab.email_tools import domain_of, split_email


def test_split_email_returns_local_and_domain():
    assert split_email("ada@example.com") == ("ada", "example.com")


def test_split_email_rejects_bad_addresses():
    with pytest.raises(ValueError):
        split_email("ada.example.com")


def test_domain_of_normalizes_domain_case():
    assert domain_of("ada@Example.COM") == "example.com"
