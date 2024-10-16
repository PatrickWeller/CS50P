# Use twttr.py from Problem Set 2,
# Reformat it to use main() and shorten(word)

# Then, in a file called test_twttr.py,
# implement one or more functions that collectively test your implementation of shorten thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_twttr.py

from twttr import shorten

def test_lower():
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_upper():
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_numbers():
    assert shorten("Hello C3PO and R2D2") == "Hll C3P nd R2D2"

def test_punctuation():
    assert shorten("Hello! Dave, are you OK?") == "Hll! Dv, r y K?"
