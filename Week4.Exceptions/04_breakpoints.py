# Breakpoints and Debugger tools


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

# Debugger

# The icon on the left of VS code with a play and bug symbol
# We can click on it, then click 'run and debug'
# Then we can select the python debugger to run the script and debug
# it will run and pause on the breakpoint.

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

main()

# We will then have options to press, from left to right:
# Continue - to move past the breakpoint, by running that line of code and following lines
# Step Over - step over the line of code at the breakpoint. It will run like normal.
# Arrow into a dot - Step into that line. Step into the main function.
# Restart process
# Stop

# We want to step into the code.
# it will now show us one step at a time what line of code is running in yellow.
# And in the top left of VS code in the 'Run and Debug' panel, some variables will start to exist as I use them.
# If I step over the second line of my code (because I don't want to step into int() or input() then
# height will be asked for in the terminal
# Once I then enter a value, height will be specified and appear as a local variable

# I will then want to step into my pyramid variable.
# Because it's my function, I want to move through each of those lines.
# n will then be the variable with value 3
# Step over a few times.
# i will be specified as 0, and then I can see my problem!
# I can see why 0 hashes are printed, then 1 then 2.
