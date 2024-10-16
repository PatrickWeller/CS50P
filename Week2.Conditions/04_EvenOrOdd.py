# Parity - Even or Odd
# + - * / %

x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# But it's good practice to define our main function
# remember we do so with def main():
# Then we write main(): with the assumption that the function exists.
# Even if it doesn't exist yet, we will go on to write it in a way that will work

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False

main()

# I've now got a function called is_even that I can reuse in any programs I like.
# And I know it will always return a Boolean (either True or False)

# But we can neaten up our is_even function to be just one line:

def is_even(n):
    return True if n % 2 == 0 else False

# We can refine it further!
# We are asking if and then forcing it to provide a boolean answer
# But we're asking a True or False question anyway, so why type out the words?
# The maths brain will produce True or False using return.

def is_even(n):
    return n % 2 == 0
