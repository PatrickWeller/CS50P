students = ["Hermione", "Harry", "Ron"]

# To index in a list also use square brackets
# They are zero indexed, remember
print(students [0])
print(students [1])
print(students [2])


# Let's improve
# Let's use a for loop, not just with numbers
# and this works if we didn't know the length of the lists

for student in students:
    print(student)


# len

# We could still use numbers if you wanted.
# range is expecting a number so can't just do range(students)
# but len gets the length of the list students, to pass to range
for i in range(len(students)):
    print(i, students[i])
# Can now see the position of each student in the list.
# will start at 0, might want to start at 1 though, so just +1

for i in range(len(students)):
    print(i + 1, students[i])
