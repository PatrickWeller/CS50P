from jar import Jar
import pytest

def test_init():
    jar = Jar()
    jar.capacity = 12
    jar2 = Jar(4)
    jar.capacity = 4

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_size():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3

def test_capacity():
    jar = Jar(4)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(4)

