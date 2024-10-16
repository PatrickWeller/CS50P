# In students4.py I have just two headings, name and house,
# I want to add people to that csv file
import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("students4.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
# If I enter something with a comma, it will add to the csv with quote marks so it doesn't get confused.

# But an alternative way is using a dictionary writer
import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("students4.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # Provide the string names of the headers
    writer.writerow({"name": name, "house": house}) # Provided the structure of the dictionary

# So with csv.writer we had to provide a set order list
# With csv.DictWriter we could change up the order, it doesn't matter
# As long as we provide in some way a value to name and house
# e.g. final line could have been:
#   writer.writerow({"house": house, "name": name})
# Still would have put them in the correct place in the file

