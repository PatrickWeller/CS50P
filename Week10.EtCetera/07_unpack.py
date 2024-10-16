# unpack.py

# What is unpacking? Let's remind ourselves.
# If someone gave their name Patrick Weller,
# We might want to unpack it to 2 variables.
# e.g.
# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

# Back to money in Gringotts
# Let's start here, with no unpacking.
def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

print(total(100, 50, 25), "knuts")

# Now...
def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "knuts")

# OK so it's not so hard coded, we're referencing a list, cool.
# It's getting a little verbose though.
# I want to just pass coins to total, like: total(coins)
# This just passes a list to 'galleons' in total(), not an integer,
# and it passes nothing to sickles and knuts.
# Causes a TypeError.

# How can I write it more briefly? Well we can use unpacking.
# We use *coins to unpack it to it's 3 individual arguments.
def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

coins = [100, 50, 25]

print(total(*coins), "knuts")

# What if we passed in the names too so the order of numbers doesn't matter so much?

def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

print(total(galleons=100, sickles=50, knuts=25), "knuts")
# Well this is silly, but if we're going to use names AND values, let's use a dictionary!
def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
# But this is super verbose again, so let's improve it!
# How can we just pass in a dictionary, and get python to find the 3 values for total()
# As we don't want python to just pass in a dictionary under 'galleons'
# Now we use **coins as it's a dictionary. 2 asterisks, not 1.
# And by the way, total() is only expecting 3 values,
# so if there's 4 key value pairs in the dictionary, that won't work.
# If we specified default values, then you could have a smaller dictionary though, of just 1 or 2 values.
def total(galleons, sickles, knuts):
    return ((galleons * 17 + sickles) * 29 + knuts)

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")

# This single and double asterisks also works in the following:
# *args, **kwargs
# If a function takes a variable number of arguments, then use these.

