# Using my own library

# We're going to use MyLibrary06.py as a library
# It has a hello function and a goodbye function, and a main function.
# Let's use the hello function.

import sys

from MyLibrary06 import hello

if len(sys.argv) ==2:
    hello(sys.argv[1])
