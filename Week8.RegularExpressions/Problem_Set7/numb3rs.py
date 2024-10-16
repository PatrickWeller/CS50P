# Numb3rs.py

# In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen,
#  275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.

# An IPv4 address is a numeric identifier that a device (or, on TV, hacker)
# uses to communicate on the internet, akin to a postal address in the real world,
# typically formatted in dot-decimal notation as #.#.#.#.
# But each # should be a number between 0 and 255, inclusive.
# Suffice it to say 275 is not in that range!
# If only NUMB3RS had validated the address in that scene!

# In a file called numb3rs.py, implement a function called validate
# that expects an IPv4 address as input as a str and then returns True or False,
# respectively, if that input is a valid IPv4 address or not.

# Structure numb3rs.py as follows,
# wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries.
# You’re welcome, but not required, to use re and/or sys.

# Also implement two or more functions in test_numb3rs.py to test validate
# the functions should begin with test_ so that the tests can be implemented with:
# pytest test_numb3rs.py

import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    is_valid = True
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for digits in matches.groups():
            digits = int(digits)
            if not (0 <= digits <= 255):
                is_valid = False
                break
        return is_valid
    else:
        return False




if __name__ == "__main__":
    main()
