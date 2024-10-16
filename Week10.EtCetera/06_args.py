# args

# We've already imported sys and used sys.argv


import sys

if len(sys.arv) == 1:
    print("meow")
else:
    print("no command line argument needed for this script")

# But let's get more complicated on the command line. Let's give switches!
# We want someone to be able to type meows.py -n 3 if they want.
# And it's nicer than 'meows.py 3' because '-n' usually means number of times.

import sys

if len(sys.arv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("no command line argument needed for this script")

# generally -n or --number. -letter --word.
# But how do i do all these checks if we have many arguments,
# And they might come in an unexpected order.
# introducing argparse! it's library.

import argparse

parser = argparse.ArgumentParser() # a class
parser.add_argument("-n") # a built in method to the ArgumentParser class
args = parser.parse_args()

for _ in range(int(args.n)): # iterate over the range of the n argument
    print("meow")

# -h or --help provides information about usage.
# Can start to built this in now.

# Let's improve it by adding a description to ArgumentParser
parser = argparse.ArgumentParser(description="Meow like a cat") # will come up with -h
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# Now we have some useful information when using -h or --help!

# But in the current state it just breaks with no -n argument
# So what do we do now?
# We can add a default value! Yes!

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", default=1, type=int) = default and type specified
args = parser.parse_args()

for _ in range(args.n): # removed int() from here because told parser earlier.
    print("meow")

#
