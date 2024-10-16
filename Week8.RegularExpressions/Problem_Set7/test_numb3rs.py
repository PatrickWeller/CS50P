# test_numb3rs.py

from numb3rs import validate

def test_ok():
    assert validate("1.2.3.4") == True

def test_over255():
    assert validate("256.2.3.4") == False
    assert validate("1.2.3.300") == False

def test_length():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False
    assert validate("0000.2.3.4") == False

def test_letters():
    assert validate("1.b.c.4") == False

