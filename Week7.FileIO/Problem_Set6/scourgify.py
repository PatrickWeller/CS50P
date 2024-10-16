# scourgify.py

# In Harry Potter 'scourgify' is used by Tonks to remove feathers and droppings from a cage.
# Data, too, often needs to be “cleaned,” as by reformatting it,
# so that values are in a consistent, if not more convenient, format.
# Consider, for instance, this CSV file of students, before.csv, below:

#name,house
#"Abbott, Hannah",Hufflepuff
#"Bell, Katie",Gryffindor
#"Bones, Susan",Hufflepuff
# etc.

# Even though each “row” in the file has three values (last name, first name, and house),
# the first two are combined into one “column” (name), escaped with double quotes,
# with last name and first name separated by a comma and space.
# Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge,
# since it’d be strange to start a letter with:
######## Dear Potter, Harry,
# Rather than with, for instance:
######## Dear Harry,

#In a file called scourgify.py, implement a program that:
# Expects the user to provide two command-line arguments:
# 1 - the name of an existing CSV file to read as input, whose columns are assumed to be,
# in order, name and house, and
# 2 - the name of a new CSV to write as output, whose columns should be, in order,
# first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name.
# Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments,
# or if the first cannot be read, the program should exit via sys.exit with an error message.
import sys
import csv
import os

def main():
    check_arguments()
    input = sys.argv[1]
    output = sys.argv[2]
    check_files_exist(input)
    clean_up(input, output)

def check_arguments():
    if not len(sys.argv) == 3:
        print("Requires 2 command-line arguments")
        sys.exit(1)
    else:
        pass

def check_files_exist(input):
    if not os.path.exists(input):
        print("Input file does not exist")
        sys.exit(1)
    else:
        pass

def clean_up(input, output):
    with open(input) as before, open(output, "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            a, b = row["name"].split(", ")
            row["first"]= b
            row["last"] = a
            writer.writerow(
                {
                    "first": row["first"],
                    "last": row["last"],
                    "house": row["house"]
                    }
            )

main()
