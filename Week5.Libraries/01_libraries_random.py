# libraries

# Sharing code through libraries, which we do by way of modules
# Allowing us to reuse code

# Well python comes with a range of libraries/modules.
# But you don't have access to the functions inside them automatically like print()
# The functions are tucked away in the modules
# You have to deliberately load them

# Somewhere in a computer harddrive there is probably a python 'random' library
# This allows you to do random number generation.

# docs.python.org/3/library/random.html

###### import #####

# Modules can be accessed using the import function
# Let's say we want to use a function we've read about in the documentation:
# random.choice(seq)
# This function chooses from a list or list like object you give it.

# Let's say i want to create a flip coin function.

import random

coin = random.choice(["heads", "tails"])
print(coin)

#### from ####

# An alternative to import
# 'import random' will import ALL of random
# AND i then need to recall it as random.choice()

# Using 'from' we then bring the 'choice' into our function vocab
# Could be an issue if I already had my own function called choice though
# But this makes code a lot neater

from random import choice

coin = choice(["heads", "tails"])
print(coin)

#### random integer ####

# random.randint(a,b)
# Get a random integer between a and b

from random import randint

dice = randint(1, 6)
print(dice)

### shuffle a list ####

# random.shuffle(x)
# This shuffles the list actually given to you

import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)
for card in cards:
    print(card)

