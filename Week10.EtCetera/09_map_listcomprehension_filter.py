### map.py ####

# We started with procedural programming
# Then object oriented programming
# Then saw hints of a third paradigm, functional programming (no side effects)
    # Saw this with the sort funtion, and lambda function.

# yell.py
def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__" :
    main()

# This is OK but yell only expects one phrase right now, what about more...
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # Use * To not print as a list, but print the values in the list

if __name__ == "__main__" :
    main()

# But right now I'm passing into yell a list, which isn't great, not convenient.
# Let's make use of what we've learned.
def main():
    yell("This", "is", "CS50")  # No longer a list

def yell(*words):   # Passing in as many positional arguments as I want
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__" :
    main()

# Python comes with a function called 'map', allowing you to apply one function,
# to every element of a sequence, like a list.
# Like applying upper to every object.
# map(function, iterable, ...)

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words) # Notice we don't use words.upper()
    print(*uppercased)

if __name__ == "__main__" :
    main()

# Can now solve in a way that's even more pythonic!
# List Comprehensions
# creating a list on the fly using some logic

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] # saves us a few lines of code.
    print(*uppercased)

if __name__ == "__main__" :
    main()


# Take the program below for listing all students in gryffindor, sorted.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
# Notice we have a conditional when making our list, if student["house] = gryffindor.
# We can simplify the code and make it more elegant.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Now look at this beauty!!
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)


# So 'map' ran a function for every element of a sequence.
## But 'filter' has one more functional aspect.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor": # returns True or false.

gryffindors = filter(is_gryffindor, students)
# Filters first argument to figure out whether True or false,
# Notice we've just named the function, not called it with is_gryffindor()
# Asking should it be included

for gryffindor in gryffindors:
    print(gryffindor["name"])

# And finally to sort the list of dictionaries we can do that too.
# We replace the last 2 lines of code with:

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
