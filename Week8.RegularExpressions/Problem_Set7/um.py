########## Um... um.py

# It’s not uncommon, in English, at least,
# to say “um” when trying to, um, think of a word.
# The more you do it, though, the more noticeable it tends to be!

# In a file called um.py,
# implement a function called count that expects a line of text as input as a str
# and returns, as an int, the number of times that “um” appears in that text,
# case-insensitively, as a word unto itself, not as a substring of some other word.
# For instance, given text like hello, um, world, the function should return 1.
# Given text like yummy, though, the function should return 0.

# And create a file called test_um.py with three or more functions to test count()
# The tests should start with test_
# Can run it with
# pytest test_um.py

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    while True:
        new = re.sub(r"\b[uU][mM]\b", "", s, 1)
        if new != s:
            count = count + 1
            s = new
        else:
            return count



if __name__ == "__main__":
    main()
