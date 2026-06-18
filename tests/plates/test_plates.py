from plates import is_valid

def test_start():
    assert is_valid('CS50') == True
    assert is_valid('50') == False

def test_length():
    assert is_valid('OUTATIME') == False
    assert is_valid('H') == False

def test_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
    assert is_valid('AAA022') == False

def test_schar():
    assert is_valid('PI3.14') == False

