# Printing a shape...

# This code let's me print a column of 3 blocks like you would see in mario
# I've created print_column as this might be something I want to do a few times dynamically
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

# And at this point I can change the exact nature of what print_column does
# And main doesn't need to know that, nothing changes in main if I change print_column

# Well what if I want to print some floating blocks with coins in them

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# Now the two scripts are fine, though they don't work together right now.
# But what if there are even more shapes, perhaps a 3x3 block to jump over.
# I would need to print from top to bottom like a printer would.

def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            # print a brick
            print("#", end="")

        # print a blank new line after each row is done
        print()

main()


##
print()
# Let's tighten it up further though


def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        # We don't yet know what print row is but we'll sort that out later on,
        # We will just assume we've got printing a row covered
        print_row(size)

def print_row(width):
        print("#" * width)

main()
