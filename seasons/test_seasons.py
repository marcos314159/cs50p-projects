from seasons import is_date_valid, in_minutes, convert
import pytest


def main():
    test_is_date_valid()


def test_is_date_valid():
    assert is_date_valid("1111-11-11") == (1111, 11, 11)
    assert is_date_valid("2025-10-01") == (2025, 10, 0o01)
    with pytest.raises(SystemExit, match="Invalid date"):
        assert is_date_valid("2030-05-10")
    with pytest.raises(SystemExit, match="Invalid date"):
        assert is_date_valid("1950-13-02")
    with pytest.raises(SystemExit, match="Invalid date"):
        assert is_date_valid("1500-08-33")


def test_in_minutes():
    assert in_minutes("1 abacaxi") == 1440


def test_convert():
    assert convert("1") == "one"
    assert convert("365") == "three hundred and sixty-five"
