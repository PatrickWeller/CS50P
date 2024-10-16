# Dictionary comphrensions;
# Can create a dictionary on the fly without making it old-school,
# you don't need to make an empty dict and create a for loop etc.

# So this code creates student dictionaries, within a list.
students = ["Hermione", "Harry", "Ron"]
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
print(gryffindors)



# Let's improve:
students = ["Hermione", "Harry", "Ron"]
# create a list of dictionarys. Each dictionary is a student, for student in students
# notice the square and curly brackets.
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)


# What if instead of a list of dictionaries, I want a large dictionary,
# where the key is the name, and the house is the value.
# (Assuming no duplicate names btw)
students = ["Hermione", "Harry", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
