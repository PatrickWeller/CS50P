# test_plates.py

from plates import is_valid

def test_start2letters():
    assert is_valid("A1111") == False
    assert is_valid("1111") == False
    assert is_valid("AA1111") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA1111") == False

def test_numberslast():
    assert is_valid("AA11AA") == False

def test_startnotzero():
    assert is_valid("AA0111") == False

def test_punctuation():
    assert is_valid("AA.123") == False
