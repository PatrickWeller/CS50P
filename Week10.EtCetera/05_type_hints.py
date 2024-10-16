#### type hints ####

# Python is a dynamically typed language.
# It's not strongly typed.
# Generally python figures out whether we are providing an int, float, str, etc.
# We just assign variables a name and a value, and python does the work.

# In C, C++, Java, the programmer specifies the type of variable.
# Helps you detect bugs more regularly.
# We can provide hints as to the type of variable, but generally works it out.

# There is a tool we can use to make sure the variable type is correct.
# Documentation
    # library/typing.html.

# Program mypy is one that can check the types.
    # pip install mypy
# Documentation
    # mypy.readthedocs.io

def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# This won't work as input is always a 'str'.
# I could do:
int(input("Number: "))

# But let's instead use a type hint:
def meow(n: int): # See this line.
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# Then run 'mypy meows.py'
# And mypy finds an error, with a row number,
# and says that "str" is the wrong type.
# So mypy is something for us to run to check for bugs.

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = input("Number: ") # Now added this type hint
meow(number)
# Error found a line earlier now.

# Then can see we should incorporate:
int(input("Number: "))
# Rerun mypy and see no issues.

###### BUT...
# now what if we assumed meow(number) would RETURN meows
# instead of printing meows.
# Because functions normally return values.
# So suppose I wrote:
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# this would print:
meow
meow
meow
None
# None is the default return value of a function if no return is specified.
# So how could I fix this mistake?
# Well inform myself that this function returns None.
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
# Then run it on mypy.
# Mypy knows that I'm asking to print(meows) which won't do anything valuable.

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="") # fix minor aesthetic bug of final new line.


#doc strings

"""
Meow n times.

:param n: number of time to meow:
:type n: int
:raise TypeError: If n is not an int
