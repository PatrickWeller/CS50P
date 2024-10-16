# plates.py

# In Massachusetts, home to Harvard University,
# it’s possible to request a vanity license plate for your car,
# with your choice of letters and numbers instead of random ones.
# Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”

# “… vanity plates may contain a maximum of 6 characters (letters or numbers)
# and a minimum of 2 characters.”

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate;
# AAA22A would not be acceptable.

# The first number used cannot be a ‘0’.”

#“No periods, spaces, or punctuation marks are allowed.”


# In plates.py,
# implement a program that prompts the user for a vanity plate
# and then output Valid if meets all of the requirements
# or Invalid if it does not.
# Assume that any letters in the user’s input will be uppercase.

# Structure your program per the below,
# wherein is_valid returns True if s meets all requirements
# and False if it does not.
# Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call
# (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if rule1(s) and rule2(s) and rule3(s) and rule4(s) and rule5(s):
        return True
    else:
        return False

def rule1(s):
    s2 = s[:2]
    return s2.isalpha()

def rule2(s):
    l = len(s)
    return 1 < l < 7

def rule3(s):
    zero_pos = s.find("0") # returns -1 if not found
    x = 0
    for c in s:
        if c.isdigit():
            break
        else:
            x = x + 1
    return x != zero_pos

def rule4(s):
    digit_present = False
    for i in range(len(s)):
        if s[i].isdigit():
            digit_present = True
            ending = s[i:]
            break
        else:
            pass

    if digit_present == False:
        return True
    else:
        for char in ending:
            if char.isalpha():
                return False
                break
    return True


def rule5(s):
    return s.isalnum()

main()
