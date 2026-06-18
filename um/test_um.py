from um import count
import pytest

def main():
    test_count()

def test_um():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("um um") == 2
    assert count("u") == 0
    assert count("m") == 0

def test_word():
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_space():
    assert count(" um ") == 1

def test_nonaplha():
    assert count("um...") == 1
    assert count(".um") == 1
