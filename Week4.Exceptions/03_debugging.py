# We want to create a script for printing # symbols
# which represent those stair blocks at the end of a mario level
# Here is our script


def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

main()

# but if we ran this code as it is,
# and when asked for an input we say 3
# our result will be

#
##

# Which is maybe not what we wanted.
# There's a blank line, then 1 hash, then 2 hashes


# How would we systematically go about fixing this bug?

# Well let's ask first, what if 'i' is wrong?
# So why don't I temporarily print out 'i' along with the hashes
# print() can be useful for figuring out bugs

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end=" ")  # now we will print the value of i
        print("#" * i)

main()

# The outcome when entering 3 would be this

0
1 #
2 ##

# Now I remember, ah, i will start from 0
# Now let's remove printing i and then fix it by increasing the value of i.

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1)) # we're increasing the value of i by 1

main()

# New output
#
##
###

# yay! Print() is our first friend when debugging code.
# We're trying to see what the computer sees.
# But we need better tools than that.
# We might put print() in the wrong place
# Or be confused what value we are printing
# Let's return to our original code
# In our next script

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

if _name_ == "_main_":
    main()

# We are now looking at the activity bar to the left of VS code.
# Integrated Development Environments (IDEs) often come with built-in debuggers.
# It empowers you to solve bugs yourself.


# Breakpoints

# Let's you specify what line of code you want to pause or break execution of the program.
# Want to slow down the execution of the program so it doesn't happen all quicker than I can manage.
# Hover over to the left of the line number
# Click the red button, it will become bright and create a breakpoint
# So we can pause execution of code before main() is called for example.
# by doing it one the line that runs main()

# The icon on the left of VS code with a play and bug symbol
# We can click it to 'run and debug'
# it will run and pause on the breakpoint.

