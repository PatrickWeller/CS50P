# game.py

# I’m thinking of a number between 1 and 100…

# What is it?
# In a file called game.py, implement a program that:

# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    # If the guess is the same as that integer, the program should output Just right! and exit.

from random import randint

while True:
    level = (input("Level: "))
    try:
        level = int(level)
        if level > 0:
            target = randint(1, level)
            break
    except ValueError:
        pass

while True:
    guess = input("Guess: ")
    try:
        guess = int(guess)
        if guess < 0:
            pass
        elif guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            break
    except:
        pass

print("Just right!")

