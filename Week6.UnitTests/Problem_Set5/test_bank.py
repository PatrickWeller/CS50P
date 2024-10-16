# In bank.py from Problem set 1,
# reformat it to make use of main(), and value(greeting)
# Then implement 3 or more functions in test_bank.py
# to test your implementation of value thorouglhy.

from bank import value

def test_hello():
    assert value("hello") == 0
    assert value(" hello ") == 0
    assert value("Hello") == 0
    assert value("Hello, there") == 0

def test_h():
    assert value("hi") == 20
    assert value(" hi ") == 20
    assert value("Hi") == 20
    assert value("Hi, there") == 20

def test_other():
    assert value("123") == 100
    assert value("Orange") == 100
    assert value(".Hello") == 100
    assert value("/Harry") == 100
