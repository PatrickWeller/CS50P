# Reimplement fuel.py from problem set 3,
# Then in a file called test_fuel.py
# implement two or more functions that collectively test your
# implementations of convert and gauge
import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    with pytest.raises(ValueError):
        convert("10/2")  # Should raise ValueError because 10 > 2
    with pytest.raises(ValueError):
        convert("dog/cat")  # Should raise ValueError because "dog" and "cat" are not integers
    with pytest.raises(ValueError):
        convert("3")  # Should raise ValueError because it's not in "X/Y" format
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Should raise ZeroDivisionError because division by zero is not allowed


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
