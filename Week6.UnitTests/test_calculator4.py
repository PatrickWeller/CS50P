## Make sure I do:
# pip install pytest
# in the terminal first

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# all 3 of these will run automatically, even if the first one fails.

# For this final test we need something other than assert
# so let's import the pytest library
import pytest

def test_str():
    with pytest.raises(TypeError):
        square("cat")
