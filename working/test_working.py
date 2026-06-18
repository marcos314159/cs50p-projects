from working import convert
import pytest

def main():
    test_working()

def test_assertions():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_errors():
    with pytest.raises(ValueError):
        convert("12 PM 12 AM")
    with pytest.raises(ValueError):
        convert("13 PM to 13 AM")

if __name__ == "__main__":
    main()
