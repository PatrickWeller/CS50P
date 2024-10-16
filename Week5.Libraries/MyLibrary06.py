# my_library

# We might want to bundle up code we use all the time and make it our own package
# Or to share it with others
# So this file is our library
# It can't be named starting with a number or maybe just 0 it seems.
# And it can't have underscores either.

# We will access it in 07_using_my_library.py
# and seek to only use the hello function

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# I can't just call main though
# As when I call for the library it will read it from top to bottom and run the main
# So:
if __name__ == "__main__":  # __name__ is a variable that will auto set to main if ran from the command line
    main()                  # But if I import the module/file then __name__ won't be set as main.
                            # So main() won't get called. And I can call for just the hello function
                            # or the goodbye function.
