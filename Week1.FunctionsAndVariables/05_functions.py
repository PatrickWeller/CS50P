# Create our own functions using def
# Everything indented is in my new function hello
#I've said that hello should be passed an argument which will be called who
def hello(who):
    print("hello,", who)

name = input("What's your name? ")
# I've passed the variable name to the hello function, so name is functioning as who
hello(name)


#What if I ever run hello but don't pass it a value for who?
#I can assign who by default like so, so it doesn't bug out
def helloagain(towho="world"):
    print("hello,", towho)

helloagain()
helloagain(name)

# If we have to define a function before calling it, does that mean we need to create
# all our functions at the top of a file, then write the bulk of code at the bottom?
# That can feel like writing code in reverse.
# We want the main part of our code at the top
# How can we fix this?
# We define our main function first! But only call it at the end

def main():
    name2 = input("What's your name?")
    hello3(name2)

def hello3(person="world"):
    print("hello, ", person)

main()

# Note, if I define a variable in the main function, I can only use it in my main function
# it doesn't exist in the so-called scope

# Can finally use the return function to return a value
# let's start from the beginning.

def main2():
    x = int(input("What's X? "))
    print("x squared is", square(x))

#The return function allows us to take the squared number and then pass it to another function,
# AKA to the print function in main2
def square(n):
    return n*n    #could also do pow(n, 2)  or n ** 2

main2()
