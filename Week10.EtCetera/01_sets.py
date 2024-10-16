##### sets ####

# Like a list, but specifically can't have any duplicates

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# What are all the unique houses in hogwarts?

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# This is totally fine, an OK way of solving the problem.
# But I'm actually reinventing the wheel by not using a set.

# By using a set I can eliminate any duplicates!
print("")

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
