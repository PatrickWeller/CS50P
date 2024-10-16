# Exceptions  - Introducing Try and Except

# Exceptions are not good things in your code.

# Types of error

# SyntaxError: unterminated string literal (detected at line 1)
# SyntaxErrors are entirely on us to figure out and fix. We did something wrong in the first place

# Runtime Errors
# Whilst running there was an error, perhaps a user put in the wrong input
# We need to try and figure out where these can occur and account for them

# Good to try fringe cases and fringe numbers etc.
# If a script needs a number, try it with 50, but then try it with 0, then -50, then 0.5, and then "dog".

# E.g. This script will produce an error if ran with "dog"
# x = int(input("What's x?: "))
# print(f"x is {x}")

# The error will be ValueError: invalid literal for int() with base 10: 'dog'
# literal is just something typed in.

# We could say we want a number, but that's not good enough.

# try and except
# try something, and if an exception happens, then do something else

try:
    x = int(input("What's x?: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# It would be poor practice to just say
# except :
# Because then you are catching all errors,
# but not anticipating or figuring out what types of error they are.

# Technically we can improve our code even more
# We want to only 'try' the one line of code that can produce an error.
# But here we are trying 2 lines.
# We could do this therefore:

try:
    x = int(input("What's x?: "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# But this introduces a whole new error when entering 'dog'
# NameError: name 'x' is not defined
# NameError tends to refer to your code, perhaps doing something with a variable you shouldn't be
# In this case, if you can't define x as an integer, then it won't have actually specified x yet
# The error occurs on the right side of that equals sign, so x is not defined, value is copied to the left
# so when printing there's no x to recall.

# 'try' also accepts 'else'
# If there's no exception, then proceed.
try:
    x = int(input("What's x?: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Let's refine it more, and re-ask the question with a loop for a new value of x
# Introducting 'break' to break out of a loop.
# and we will shove it in the 'else' clause
while True:
    try:
        x = int(input("What's x?: "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

# We can even refine it further
# You either get an error and do the except, or you just break

while True:
    try:
        x = int(input("What's x?: "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")

# What if I want a function to reuse that gets an integer from the user?
# let's do that in the next script
