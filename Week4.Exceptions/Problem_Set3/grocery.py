# grocery.py

# Suppose that you’re in the habit of making a list
# of items you need from the grocery store.

# In a file called grocery.py,
# implement a program that prompts the user for items,
# one per line, until the user inputs control-d
# (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase,
# sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.

groceries = {}

def main():
    add_to_list()
    print_groceries()

def add_to_list():
    while True:
        try:
            new = input().upper()
        except EOFError:
            break
        if new in groceries:
            groceries[new] = groceries[new] + 1
        else:
            groceries[new] = 1

def print_groceries():
    for item in sorted(groceries):
        print(groceries[item], item)

main()
