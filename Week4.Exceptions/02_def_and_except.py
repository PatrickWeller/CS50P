# We want a function that asks the user for an integer again
# And we want to reuse this function
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            return x   # return will return the value AND break
        except ValueError:
            print("x is not an integer")

main()

# Can I tighten up get_int() though?
# Potentially this could work

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? ")) # we#re never defining x
        except ValueError:
            print("x is not an integer")

main()

# Now a further step
# What if instead of repeatedly saying "x is not an integer"
# We just want to pass and ask for an input again
# We can use 'pass'
# You can argue it's worse as it's less explicit
# But kind of neater.

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass

main()

# We could by the way just use an if statement to check if we've had a number inputted
# rather than trying to catch errors and account for them
# but the pythonic conventions is not to have if if if if elif elif else
# but to just go 'eh let's try it' and then catch and handle any errors


# Final refinements
# Let's not hard code 'X'
# We might not always want to be asking for x with our get_int function
# We might want to use our get_int() function to ask for x and then ask for y.
# so we make the get_int() function require a prompt that you provide
# This prompt can ask for x or we can make it an ask for y etc.

def main():
    x = get_int("What's x? ")  # changed line.
    print(f"x is {x}")

def get_int(prompt):            # changed
    while True:
        try:
            return int(input(prompt))   # changed
        except ValueError:
            pass

main()

# You can also even 'raise' exceptions using 'raise'
# More on that another time.

