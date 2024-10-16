## fuel.py

# Reimplement fuel.py from problem set 3 to tell you how full your fuel tank is.

# Prompt the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
# and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank.
# If, though, 1% or less remains,
# output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains,
# output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y,
# or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# But restructure your code to include: main(), convert(fraction), gauge(percetange).
# convert expects a str in x/y format where X and Y are integers.
# If X and/or Y are not integers, then convert should raise a ValueErrpr
# if Y is 0, then convert should raise a ZeroDivisionError
#######
import sys

def main():
    while True:
        reading = input("Fraction: ")
        try:
            percentage = convert(reading)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please try again.")
    output = gauge(percentage)
    print(output)


def convert(reading):
    fraction = reading.split(sep="/")

    # Catch errors
    if len(fraction) != 2:
        raise ValueError

    num, denom = fraction[0], fraction[1]
    if not (num.isdigit() and denom.isdigit()):
        raise ValueError

    num = int(num)
    denom = int(denom)

    if denom == 0:
        raise ZeroDivisionError
    elif num > denom:
        raise ValueError

    return round((num/denom)*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
