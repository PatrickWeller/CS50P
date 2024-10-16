#return values and variables
name = input("What's your name? ")   # Copy what's on the right and hand it to what's on the left.
print("hello,", name )   #When passing multiple arguments to print it auto inserts a space between them
print("hello, " + name)  #When using + you need to ensure you've included a space, as it just becomes one big argument

# Pseudocode - not sure how to write program yet. But outline steps with comments.

#This prints on two lines
print("hello, ")
print(name)

#if i go to docs.python.org I find the print documentation. Find this:
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#This shows every potential argument. These are the parameters of the function.
# *objects means you can pass any number of arguments
# sep=' '   means multiple arguments are separated by a space
# end='\n'  means end with a new line

#so can do this
print("hello, ", end='')
print(name)

#What if we want to print a quote?
#We can use double quote marks in single quote marks
print('hello, "friend"')
# OR we can use a back slash character which represents an escape character
print("hello, \"friend\"")


#Most elegant solution to all this though
print(f"hello, {name}")  #f at the start means this is a special string


# What if someone enters their name with spaces, and without capitals?
# Ask user for wife's full name
wifename = input("What's your wife's full name?")
# Remove white space from start and end of string
wifename = wifename.strip()
# Will only capitalise the first name
wifename = wifename.capitalize()

print(f"hello, {wifename}")

# Will capitalise both names
wifename = wifename.title()

print(f"hello, {wifename}")

# Can chain them
# wifename = wifename.strip().title()
# Does them functions from left to right.
# So most succinct is
brothername = input("What's your brothers's full name? ").strip().title()

print(f"hello, {brothername}")

# Using split to separate parts of a string
mothername = input("What's your mother's full name? ").strip().title()

#Splits up mothername by space
first, last = mothername.split(" ")

print("hello,", first)
