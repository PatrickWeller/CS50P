# Storing header rows can be very helpful
# in students3.py I've added headers
# I can then use not just a csv reader, but a csv dict reader.
# it wil read each line, not as a list of items, but as a dictionary of items,
# using the headings
import csv

students = []

with open("students3.csv") as file:
    reader = csv.DictReader(file)  # Changed reader to DictReader
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})  # Changed how info is accessed

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
# Code is now a bit more robust. Someone could open the CSV in excel, switch the columns around etc.
# Now safe against that. Coding defensively.
# We can add extra columns to the dictionary too
# But the DictionaryReader will never be broken in this case

