# command line arguments

# Providing inputs/arguments in the command line, not in the file

# e.g.
# python hello.py .......


#### sys ####
# We're going to work with the 'sys' module
# This module gives us access to values typed on the command line

# docs.python.org/3/library/sys.html

### sys.argv ####
# This is a variable that exists for you in the sys module already
# This variable, meaning argument vector,
# describes all the words the human types in at the prompt before hitting enter.
# It's a list


### name.py ###

import sys
print("hello, my name is", sys.argv[1])

# I'm hoping the user knows how this script works and will give me just 1 input
# Previously we said lists are zero indexed. But sys.argv[0] is the name of the program
# If no name is entered because the user doesn't know, there will be an exception, an index error
# lets try to handle the exception


import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Required a name argument")

# Could improve further
# By removing the need to try, and accounting for too many arguments

import sys

if lens(sys.argv) <2:
    print("Too few arguments")
elif lens(sys.argv) >2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# And by the way, if someone wants to enter their full name as an argument,
# they can put their name in quotes in the command line.

# Let's improve further!
# We generally want error handling separated from our main code
# our main code is in our else statement. that's weird.

# Instead we want to handle our errors and exit out of the code quick if there is one,
# And have the main code underneath if no errors were detected
# so use sys.exit to exit early.
import sys

if lens(sys.argv) <2:
    sys.exit("Too few arguments")
elif lens(sys.argv) >2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


#### slices #####

# Slices are subsets of data or strings or lists

# If we want the user to input several first names
# do this

import sys

if lens(sys.argv) <2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # Start at index 1, not 0, and go to end of list
    print("hello, my name is", arg)

# If we had done [1:-1] Then that would start from the second value, and end on the second last value
