#### *args and **kwargs

# The single asterisk to unpack a list,
# and a double asterisk to unpack a dictionary,
# also appears here:
# *args, **kwargs

# If a function takes a variable number of arguments, then use these.

def f(*args, **kwargs):
# will take a variable number of positional arguments
# and a variable number of key word arguments.
    # Using this to diagnose what the syntax does for now!
    print("Positional:", args)

# Call the function, with a variable number of args,
# and it still works OK.
f(100, 50, 25)
f(100, 50, 25, 5)

def g(*args, **kwargs):
    print("Named:", kwargs)

g(galleons=80, sickles=40, knuts=20)

# Outputs:
# Positional: (100, 50, 25)
# Positional: (100, 50, 25, 5)
# Named: {'galleons': 80, 'sickles': 40, 'knuts': 20}

# args by default is a list of positional arguments
# kwargs by default is a dictionary of named arguments.

# We've been able to use the print() function with no, one or more arguments
# because the print documentation says print is defined something like this:
def print(*objects, sep=' ', end="\n", ...):
    for object in objects:
        ...

