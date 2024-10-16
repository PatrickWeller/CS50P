# Bigger dictionaries

# What if we want to basically store a table with many columns.
# E.g. not just one value per key, but multiple values.
# E.g. A name, a house and a patronus

# Well what if instead of our keys being the student names like below...
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}
# What if we made every student their own dictionary? Then house and patronus would be the keys.

# Treat it like a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None}   #None is special key word in python, so we know we didn't just forget to enter a value.
]

# Now I can do better loops.
for student in students:
 print(student["name"])

# Or
for student in students:
 print(student["name"], student["house"], student["patronus"], sep=", ")
