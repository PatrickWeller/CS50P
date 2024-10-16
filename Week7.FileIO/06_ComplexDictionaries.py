# So we now have a file, students2.csv
# Containing student names and where they live

# See below:
# Harry,Number Four, Privet Drive
# Ron,The Burrow
# Draco,Malfoy Manor

# Now there is the issue of an extra comma in Harry's address


#students = []

#with open("students.csv") as file:
#    for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home", home}
#         students.append(student)
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")



# This code will produce a ValueError, because of the 3 values in Harry's dictinary
# How do we get around commas that are naturally in our grammar?
# Could change our separator, such as a vertical bar
# Or could put quotes around any string, but then I have to be a lot more clever with split
# Other people have clearly had this problem before!

# Let's see if there's a library in python that exists to read and/or write CSV files?
# There is, csv
# It is good at working our where my issues are...
# Not really understanding this bit all too well
######### This function did NOT work as David said it would.... Disaster
import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home}) # Assigns the first and second value in each row to a dictionary

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#### Did not work as David said
