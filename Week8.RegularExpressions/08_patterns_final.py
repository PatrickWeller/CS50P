##### hexadecimal code

# hexadecimal codes encode colours
# e.g. #0076BA
# the first two digits, how much red is in the colour
# middle two, how much green
# final two digits, how much blue
# Range from 00 to FF
# white #FFFFFF, black #000000

import re

def main():
    code = input("Hexadecimal colour code: ")

    pattern = r"^#[0-9A-Fa-z]{6}$"

    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")

main()

