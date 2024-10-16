# So I have my file names.txt
# but how do I read it?

with open("names.txt", "r") as file: # read mode, though this is default, so not needed
    lines = file.readlines()

for line in lines:
    print("Hello, ", line.rstrip())
# another option to remove additional new lines is:
#   print("Hello, ", line, end="")


# But here we are reading all of the lines, then iterating over all of the lines
# We can make our code better
with open("names.txt", "r") as file:
    for line in file:       # This bypasses readlines()
        print("Hello, ", line.rstrip())

# What if we then wanted our printing to be sorted?
# Well we can't now use the previous code, I need to:
# Read, then sort, then print.

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# If working with files but you want to change that data in someway,
# Then this is a common way of dealing with it
# Taking file data, turning it into a list
# Then manipulating that list via sorting etc.

# What if we wanted the file itself to be sorted?
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello, ", line.rstrip())

