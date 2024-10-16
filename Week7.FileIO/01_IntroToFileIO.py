# File I/O  Input and Output

# Thus far all our programms have stored information in variables in the memory.
# There's been no permanence of these values
# No files have been accessed

# File IO is all about reading from, and writing to, files themselves

# names.py

names = [] # empty list

for _ in range (3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")

# This file uses 3 names, it can be burdensome to reinput the same names again and again
# So let's try and save this list to a file so that we have it next time we load up VScode
