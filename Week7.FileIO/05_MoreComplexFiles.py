# What if we wanted to store more complex info than just a list of names?
# We might want names connected to other information, right?
# probably want a csv file, comma separated values

# e.g.
# Hermione,Gryffindor
# Draco,Slytherin
# Harry,Gryffindor

# We have this info in students.csv
with open("students.csv") as file:
    for line in file:
        # Will strip new line, then split line based on comma, creating a list
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# An alternative to make it more readable
with open("students.csv") as file:
    for line in file:
        # We know .split() returns a list, and we know there will be 2 variables each line
        # So let's just assign them right away, and not make a list called row like before
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# But what if I want to sort the names and print them in order with their houses?
# Here's a slightly hacky way of doing it...
# I'm sorting full sentences
students = []

with open("students.csv") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# I would rather sort by the individual student names, sort them, then get their houses
# Let's create dictionaries!
students = []

with open("students.csv") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         student = {}
         student["name"] = name
         student["house"] = house
         students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}") # Note I'm using double, then single quotes

# Let's neaten it up
students = []

with open("students.csv") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         student = {"name": name, "house", house}   # In one line assign the key and value
         students.append(student)

for student in students:    # Can't sort students, because each student is a dictionary
    print(f"{student['name']} is in {student['house']}")

# Now let's find a way to sort the student dictionaries based on the names inside them
students = []

with open("students.csv") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         student = {"name": name, "house", house}
         students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name): # Passing the function get_name as a argument into the function sorted()
                                                # Sorted can be used with Key to tell sorted how to sort our dictionaries
                                                # get_name will be run on every dictionary in that list of dictionaries
                                                # Notice I'm not calling get_name with parentheses
    print(f"{student['name']} is in {student['house']}")

# The upside of all this:
# Because I'm using a list of dictionaries, and keeping all student data together,
# until the last minute when I'm finally doing the printing,
# I now have full control over the information itself
# I don't have to construct those sentences in advance like I hackishly did before

# Now I'm using the get_name function. But I will never used get_name function ever again.
# So I can actually pass to 'key' a lambda function, so an anonymous function, withou a name
# The syntax is weird, so bare with me
students = []

with open("students.csv") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         student = {"name": name, "house", house}
         students.append(student)

# This does the same as the get name function
# Given a student, index into the dictionary and return their name.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
