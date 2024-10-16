# professor.py - Little Professor

# One of David’s first toys as a child, funny enough, was Little Professor,
# a “calculator” that would generate ten different math problems for David to solve.
# For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4.
# If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
# If David were to answer incorrectly, the toy would display EEE.
# And after three incorrect answers for the same problem,
# the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# 1     Prompts the user for a level, n.
#       If the user does not input 1, 2, or 3, the program should prompt again.
# 2     Randomly generates ten (10) math problems formatted as X + Y = ,
#       wherein each of X and Y is a non-negative integer with n digits.
#       No need to support operations other than addition (+).
# 3     Prompts the user to solve each of those problems.
#       If an answer is not correct (or not even a number),
#       the program should output EEE and prompt the user again,
#       allowing the user up to three tries in total for that problem.
#       If the user has still not answered correctly after three tries,
#       the program should output the correct answer.
# 4     The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
# the user for a level and returns 1, 2, or 3, and
# generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random

def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        z = x + y
        num_guess = 0
        while True:
            guess = input(f"{x} + {y} = ")
            try:
                guess = int(guess)
            except (ValueError, TypeError):
                print("EEE")
                num_guess = num_guess + 1
                if num_guess == 3:
                    print(f"{x} + {y} = {z}")
                    break
                continue
            if guess != z:
                print("EEE")
                num_guess = num_guess + 1
                if num_guess == 3:
                    print(f"{x} + {y} = {z}")
                    break
                continue
            else:
                score = score + 1
                break
    print(f"Score: {score}")

def get_level():
    while True:
        n = input("Level: ")
        try:
            n = int(n)
        except (TypeError, ValueError):
            continue    # paradoxically, continue skips the rest of the loop and restarts it
        if 0 < n < 4:
            return n
        else:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)
    return number

if __name__ == "__main__":
    main()
