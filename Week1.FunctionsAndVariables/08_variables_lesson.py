# Variables

# Let's say I want to have a guessing game where a user guesses a number
# It would be worthwhile to store a users guess in my program

# assigning the value in the container called guess
guess = 10

#print out the guess
print(guess)


# Could run this with python guess.py let's say.

#guess.py
#But let's combine functions and variables
def get_guess():
    guess = 10
    return guess

# If I ran guess.py now I would get 10
print(get_guess())

# But it wouldn't be great if the user had to open the program
# just to change their guess value
# We want them to type in their guess in the terminal

#let's try again

#guess.py
def get_guess():
    guess = input("Enter a guess: ")
    return guess

print(getguess())


# Now we want to compare the guess to my number.

# Because this is a different function, I can name a variable guess
# and it has no baring on the other variable called guess
def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

print(getguess())

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")
    print(guess)
