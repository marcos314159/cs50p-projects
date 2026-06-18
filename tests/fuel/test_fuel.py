from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert('2/4') == 50
    assert convert('1/1') == 100
    assert convert('0/1') == 0
    with pytest.raises(ZeroDivisionError):
        assert convert('2/0')
    with pytest.raises(ValueError):
        assert convert('hello/hi')
    with pytest.raises(ValueError):
        assert convert('-1/3')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'
