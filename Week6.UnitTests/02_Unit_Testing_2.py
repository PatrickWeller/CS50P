# Unit Testing hello.py

# We're going to test the hello function in hello.py

# This is the original hello.py:
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()

# The issue is it doesn't actually return a value, it just prints something.
# So I can't put the following code in a test file called test_hello1.py:
from hello import hello

def test_hello():
    hello("David") == "hello, David"
# Because test_hello() won't return any value. Printing is just a visual side effect.

# As our code becomes more and more complex, it becomes best practice to not have side effects,
# such as printing, if you can avoid it.
# Especially if we want our code to be testable.

# So I've changed hello.py into hello2.py in order to show a better way that returns a value
# because we want to test these values, not side effects.
# I've done so using an f string.
# So hello() returns a value now.

# I can now run
pytest test_hello.py

# The only other option is called hello with no argument,
# so we then add a test to check the returned value if we offered no argument
# See test_hello2.py

