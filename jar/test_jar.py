from jar import Jar
import pytest
from unittest.mock import Mock


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    test_capacity()
    test_size()


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5
    with pytest.raises(ValueError):
        assert Jar(-1)


def test_str():
    jar3 = Jar()
    jar3.deposit(2)
    assert jar3.__str__() == "🍪🍪"
    jar4 = Jar()
    assert jar4.__str__() == ""


def test_deposit():
    jar5 = Jar(5)
    jar5.deposit(3)
    assert jar5.size == 3
    with pytest.raises(ValueError):
        assert jar5.deposit(3)


def test_withdraw():
    jar6 = Jar(3)
    jar6.deposit(2)
    jar6.withdraw(1)
    assert jar6.size == 1
    with pytest.raises(ValueError):
        assert jar6.withdraw(3)


def test_capacity():
    mock1 = Mock()
    mock1.capacity()
    mock1.capacity.assert_called_once()
    jar7 = Jar()
    assert jar7.capacity == 12


def test_size():
    mock2 = Mock()
    mock2.size()
    mock2.size.assert_called_once()
    jar8 = Jar()
    assert jar8.size == 0
