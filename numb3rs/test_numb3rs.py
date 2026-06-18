from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("cat") == False
    assert validate("-1.23.23.4") == False
    assert validate("256.23.43.6") == False
    assert validate("23.21.65.34.65") == False
    assert validate("23") == False
    assert validate("24.124.256.213") == False

if __name__ == "__main__":
    main()
