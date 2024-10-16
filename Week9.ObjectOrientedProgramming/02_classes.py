######## Classes.py

# Classes are custom made data types we can create
# We can give them their own names and terminology
# They act as blueprints for pieces of data.
# You can get types of data, exactly how you want.
# This is a primary feature of object oriented programming.

# see docs.python.org/3/tutorial/classes.html

# Classes have attributes.
# attributes are properties of sorts that allows you to specify values inside classes.
# access them with a dot.
# So below my attributes are name and house.
# More technically we can call those same attributes "instance variables"

# Every time you use a class, you're creating objects.

# Convention uses capital letters
# The ... is enough to create the new class.
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # I'm creating an object of the class Student.
    # If the class is a mould, an object is a copy made from that mould.
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()

# So name and house are two attributes, or instance variables.
# They are inside an object called student
# In a class/whose type is called Student.

# Let's add a bit more functionality right now.
# Because our lines like 'student.name = input("Name: ")' is a little bit manual.
# And its a bit reckless to be putting anything I want inside the student object.
# Let's standardise what the attributes can be, what sort of values you can set them as.

# As well as attributes/instance variables, we also need methods.

# methods
# classes come with methods or functions inside of them you can define
# (two underscores is a dunder.)
#__init__ is an instance method designed by python authors
# it allows you to initialise the contents of an object from a class
# This is really getting to object oriented programming.
# We're adding variables to objects.


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Now passing in arguments to the Student() function
    # Constructor code. Constructs a student object.
    # Using Student class as a template.
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()

# Where is the Student() function defined?
# Well the function that will always be called is __init__
# For the initiliasation of an object in python.
# self is the first argument given to the init method (the function in the class)
# It could be called anything but self is conventional.
# self gives you access to the current object that was just created.
# that's how you can then do self.name within the __init__ function.
# To reference the object created by init.
# self.name and self.house is then like installing into otherwise empty object,
# name and house, and storing them really in identically named instance variables
# in the object.

# So INIT does INITIALISATION of coonstructing an object for us.

# class is code.
# object is in the memory.

############# Now let's clean up our current method ###########
### Before
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# What if we want to catch errors like a user pressing enter, and not inputting any name?
# That would be a weird bug, to have an object with no name
# And there are only 4 houses, so I want one of those valid names.
# I could do all of the validation in the get_student() function
# But then that would be decoupled from the Student class.
# Let's encapsulate inside the class, all the functionality of that class.
# Let's encapsulate the validation of name and house, in the Student class.
# Especially if we have really long code,
# we will want all the house and name code in the student class, together, neatly.

# We also want to make sure that our validation doesn't just involve sys.exit(): for errors
# We don't want a code 10 minutes into running, ask for an input,
# and then cancel the code entirely if the user entered an input slightly wrong.
# So let's handle errors appropriately.
# Also we can't just return None if name is empty,
# as the object is already created by that point.
# We're going to use the word 'raise' to raise errors, but not exit the whole programme
# And then we could try to return Student(name, house), except if there's a Value Error...


class Student:
    def __init__(self, name, house):
        if not name: # if name blank. Same as name == ""
            raise ValueError("Missing name")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()
####################
# But we won't fully implement that now
# What if the house isn't one of the HP houses?


class Student:
    def __init__(self, name, house):
        if not name: # if name blank. Same as name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()

# And there are ways you could create a library of classes, in a module/package,
# And then import them into your other scripts

# You can't just do print(student) to print the student object
# It will create a message like so:
# <__main__.Student object at 0x102773e80>
# The error number is just where the object is stored in the computer's RAM

# But in the same way as __init__ we could use this other special method, __str__
# If we use __str__ and define it inside of our class, then when we call it,
# any time a different function wants to see the object as a string, it will be able to.

# So let's define a second function in our class

class Student:
    def __init__(self, name, house):
        if not name: # if name blank. Same as name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):  # By convention __str__ just takes one argument, self
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)  # Ask to print student. Because Print is hoping for a string,
                    # the object will trigger __str__ method to be called
                    #

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()


