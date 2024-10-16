# Pizza Pie!

# Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs,
#  aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

# Students tend to buy pizza by the slice,
# but Pinocchio’s also has whole pizzas on its menu too,
# per this CSV file of Sicilian pizzas, sicilian.csv, below:

#Sicilian Pizza,Small,Large
#Cheese,$25.50,$39.95
#1 item,$27.50,$41.95
#2 items,$29.50,$43.95
#3 items,$31.50,$45.95
#Special,$33.50,$47.95

# Of course, a CSV file isn’t the most customer-friendly format to look at.
# Prettier might be a table, formatted as ASCII art.
# In a file called pizza.py,
# implement a program that expects exactly one command-line argument,
# the name (or path) of a CSV file in Pinocchio’s format,
# and outputs a table formatted as ASCII art using tabulate,
# a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .csv,
# or if the specified file does not exist,
# the program should instead exit via sys.exit.

#pip install tabulate
import sys
import csv
from tabulate import tabulate

def main():
    check_arguments()
    file = sys.argv[1]
    ascii_convert(file)

def check_arguments():
    if len(sys.argv) == 2:
        if str(sys.argv[1]).endswith(".csv"):
            pass
        else:
            print("Not a CSV file")
            sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        print("Too many command-line arguments")
        sys.exit(1)

def ascii_convert(x):
    data = []
    with open(x) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    print(table)

main()



