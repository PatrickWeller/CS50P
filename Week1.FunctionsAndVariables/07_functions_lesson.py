# Functions

# Functions can produce 2 types of output
# 1 - Return Value
# 2 - Side Effect


# Side effect
def greet(input):
    if "hello" in inut:
        print("hello, there")
    else:
        print("I'm not sure what you mean")

greet("hello, computer")

# If I run this, I will see "hello there" in my terminal.
# This is a side effect.


# Return Values
# A Return value is a value that a function can pass to my program to use later on in my code.
# At the moment, my greet function doesn't return anything.
# So instead of using print that we see, we need to use return instead

def greet(input):
    if "hello" in inut:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

# If I run greet it won't show us anything
# We need to store the return value of greet with this input as a variable
greeting = greet("hello, computer")

#Now I can print that value
print(greeting)

# The advantage of return values is that I'm not limited to just using the side effect
# I can now do something like
print("Hm,", greeting)
# or if I specified a name previously
print(greeting + name)

