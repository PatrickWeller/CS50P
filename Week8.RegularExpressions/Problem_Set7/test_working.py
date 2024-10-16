# test_working.py
import pytest
from working import convert

def test_short():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_long():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_12():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_minutes():
    assert convert("6:30 AM to 7:45 PM") == "06:30 to 19:45"
    with pytest.raises(ValueError):
        convert("9:60 AM to 4:60 PM")

def test_letters():
    with pytest.raises(ValueError):
        convert("B AM to 5 PM")

def test_no_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
