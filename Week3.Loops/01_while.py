# WHILE

# Introducing while.
# while something is true, do something again and again

# If I want to say meow three times. Put up 3 fingers,
# every time you meow, lower a finger,
# only meow again if a finger is still up.

#i = 3
#while i != 0:
#    print("meow")
#    i = i - 1

# ctrl + c   stands for cancel.
# So that will stop your code running if you made an infinite loop.

# An alternative way could of course be counting up
# gets you around thinking of "not equal" which can be confusing compared to "equal".
# i = 1
# while i <= 3:
#    print("meow")
#    i = i + 1

# But we have a habit of starting from 0 in coding.
# So can change it like this: go up to 3, but not through 3.

# i = 0
# while i < 3:
#    print("meow")
#    i = i + 1

#It's very common to need to say:
# i = i + 1
# So a speedier way has been made
# i += 1

#final code
i = 0
while i < 3:
    print("meow")
    i += 1
