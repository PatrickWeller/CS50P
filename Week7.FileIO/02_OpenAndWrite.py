#########################
# Introducing 'open'

name = input("What's your name? ")

# Open a file with the name names.txt, and we want to write to it
# open assigns a file handle, so we can access that file susbequently, we're calling it file
file = open("names.txt", "w")
file.write(name)
file.close()

# Creates the file names.txt with just my name in.
# But the current code overwrites the file.
# "w" recreates the file each time it's done.
# "a" is used to append and so can be ran 3 times.

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()

# But this new file will just have 3 names in a row, e.g. PatrickMaisieJosh
# We want to add a new line.

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# But remembering to close files can actually be awkward.
# In our next file we will have another option, 'with'
# We use it to mean: With this file open, do something, then close it.
