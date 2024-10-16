# with

# We can forget to close files sometimes
# using 'with' is a more pythonic way of manipulating files
# to open them and automatically close them

name = input("What's your name? ")

with  open("names.txt", "a") as file:
    file.write(f"{name}\n")
