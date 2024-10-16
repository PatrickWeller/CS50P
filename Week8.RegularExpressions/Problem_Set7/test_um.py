# test_um.py

from um import count

def test_start_end():
    assert count("um hello") == 1
    assert count("hello um") == 1

def test_multiple():
    assert count("hi um um um hello") == 3

def test_punctuation():
    assert count(".um.") == 1
    assert count("(um)") == 1
    assert count("?um?") == 1

def test_full_words():
    assert count("bump lump stump") == 0

def test_capitals():
    assert count("UM MUM UM") == 2
