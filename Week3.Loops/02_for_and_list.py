# for and lists

for i in [0, 1, 2]:
    print("meow")

# This is shorter than the while loop to say meow 3 times. Nice.

# Lists are denoted with these square brackets

# But you don't want to type  0, 1, 2 up to a million if you want it a million times.
# So let's improve with range (that starts at 0 by deafult)

for i in range(3):
    print("meow")

# Notice that I'm naming a variable but never actually using it.
# I need a variable to count, but I'm never recalling that value.
# So python best practice would be using a single underscore
# Signals to yourself yes its a variable but you don't care about its name as you aren't using it later.

for _ in range(3):
    print("meow")

# An alternative
print("meow\n" *3, end="")   # final new line removed.

# What if we want a user to state the number of times you meow
# And we need a positive integer of course.
# We counterintuitively produce an infinite loop with ' while TRUE'
# Then ask a question and only break out of the loop if they give us a positive integer

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# But what if we want a meow function

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n   # to use n outside of this function return n outside of the loop but inside the function.

def meow(n):
    for _ in range(n):
        print("meow")

main()
