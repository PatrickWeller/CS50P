# Intro to Object Oriented Programming (OOP)

# If you learn other languages in coding, you'll learn patterns and capabilities.
# Hard to see right now.
# So far all we've done is written procedural code - procedures, functions.
# And top to bottom.

# But along the way we've encountered Functional Programming
# Passing functions around.
# We even encountered an anonymous function some weeks ago.

# Today we focus another paradigm of coding.
# Object Oriented Programming.
# Python is flexible in letting us tackle problems in several ways.
# But OOP is a great solution to problems with longer and more complex code.

# We'll start by writing code very procedurally.
# Let's start asking for a name, and their house, and print that info together.
# We'll expand it until we see problems that we don't yet have elegant solutions for.
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()

# We will improve this by just defining get_student that gets us Name and House.
# But hmm... How do we return name and house from one function called get_student()?
# We want to return them both... we could return a dictionary object...
# that might be too complicated though, any other idea?
# we just use a comma: return name, house
# but I then need to access them in the main function.

def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()

# And to be clear, within each function, I need to use the same variable names,
# but they can be different between functions. Such as just n and h in get_student()

######## Tuples #######
# So what we've done is return a tuple, a collection of values
# It's similar to a list, but a list is mutable, you can change certain parts of it.
# E.g. (0) or (1) etc.
# A tuple is immutable, you cannot change it's parts.
# So if you have no intention of changing the values, you can work with tuples.

# And to make it clear, a tuple is one value, inside of which are multiple values.
# And I've made it clear I'm working with a tuple by using a comma to separate values.
# More explicit syntax we can use would be using brackets.
# When we return (name, house) so then we know we're passing a tuple
# The tuple in main() can then be given a name

# But then how do we print out the name and house if the data isn't in variables?
# We we can treat it like a list and index into it:

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()

# So tuples can be chosen over lists when we want to code defensively.
# Increases correctness by not letting the values be changed, due to the immutability.

# Let's say we think the user could enter stuff wrong.
# Because we know Padma is from Gryffindor in the films, but Ravenclaw in the books.
# There's an inconsistency. We want to hard code it so Padma is always Ravenclaw.
# But the code below will churn out an error if we input house as Gryffindor!

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()

# TypeError: 'tuple' object does not support item assignment.
# Assignment is copying from right to left, so that is what is invalid
# Showing us that tuples are immutable.

# So we choose to either return a tuple:
# (name, house)
# or a list:
# [name, house]
# depending on if we want our code to be immutable.
# But both are accessed with square brackets:
# student[0]

# Now would a dictionary make the situation better for us?
# Well it's good for syntax, associating keys with values
# Don't have to remember [0] is name and [1] is house
# instead name is name. And house is house.

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}") # make sure to use single quotes

def get_student():
    student = {}
    student = ["name" = input("Name: ")]
    student = ["house" = input("House: ")]
    return student

if __name__ == "__main__":
    main()

# We can tighten it up though. get_student() can be a lot tighter.
# We don't need to make an empty dict, and then two keys
# We can create the dictionary on the fly like this.

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

# Now what if we wanted to fix inputs of Padma to Ravenclaw?
# You index into lists and tuples using numbers
# But you input into dictionaries using strings.

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

######## BUT #####
# All this has been hard work.
# One day we might want to capture patronus and favourite spell.
# It's all so complex now.
# What if the authors of python had just given us a data type called student.
# Then i wouldn't need to figure out whether to use a tuple, a list, or a dictionary.

# Obviously the python creators can't anticipate them all.
# But they anticipated, and gave us a general purpose tool,
# so that we can create our own data types and terminology.
# And these are called classes.


