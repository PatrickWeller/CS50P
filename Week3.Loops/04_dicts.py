# dictionaries. dicts

# They allow you to associate one thing with another thing.
# like a word with a definition
# Or a key with a value
# Like a table

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# This solution to a problem using 2 lists is not good.
# We have to agree the first position of each list lines up with each other
# And what if we want to have a list for patronuses, and surnames and so on.

# Use curly brackets for a dictionary
# keys on left, values on right

students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}

print(students["Hermione"])  #Look up Hermione, and get me her value

# We can make it more dynamic though.

# This would only print the keys
for student in students:
    print(student)

# This would print the key and value
for student in students:
    print(student, students[student])

# Can add a separator to make it neater
for student in students:
    print(student, students[student], sep=",")

