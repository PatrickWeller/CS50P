# True power comes from producing our own methods in a class
# Here is our current version

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()


###  We'll add patronus to __init__()
### define self.patronus
### and add it to the get_student function
### won't print it out yet though.

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name, house, patronus)
    except:
        ...

if __name__ == "__main__":
    main()

# But you see we don't just want to be remembering/storing information about students,
# We don't just want instance variables/attributes we keep creating
# We want functions built in, a.k.a methods. Functions in classes are called methods.
# We've seen the __init__ and __str__ functions/methods already.
# Python calls them automatically for you if you define them.
# But what if we make our own.

## We're going to create the charm function


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "✨"

def main():
    student = get_student()
    print("Expecto Patronum") # new output
    print(student.charm())  # new output. So calling the function outside the class

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name, house, patronus)
    except:
        ...

if __name__ == "__main__":
    main()

# So to reiterate some points:
# __init__, __str___, and charm are all functions, known as methods, inside a class.
# By convention, all methods in a class python expects to pass in at least one argument
# And that argument will always be a reference to the current object
# So it should always, at the least, take in the argument called self.

# Right we're going to revert to remove all the patronus stuff and start fresh,
# in order to look at some other capabilities

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()

# So what now? Well our use of classes are not very robust currently.
# We could circumvent our error checking (of no name, or a non-hogwarts house).
# I could do so with this code:

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

# We can still read and change these attributes with this familiar dot notation
# This will circumvent the 'if' condition in our __init__ method
# Because that error checking is only for initialisation, when we create the object.
# Nothing stops me from changing name or house after.
# So let's code a bit more defensively.

###### Introducing Properties ######
    # An attribute with more defense mechanisms
    # More functionality implemented by programmers to prevent mess ups
    # Use the keyword: @property
    # @ is syntax that allows you to decorate functions
    # @ is therefore known as a decorator
    # it edits the behaviour of other functions

# So let's create a property called house
# below __init__ and __str__
# Confusingly I'm creating 2 functions, both called house...
# One just returns self.house
# The other adds error checking. then makes self.house = house

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    # A function for a class that gets some attributes
    @property
    def house(self):
        return self._house

    # Setter
    # A function for a class that sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

# What we're trying to say is:
# In order to access an attribute we want you to go through a function
# And in order to set some attribute we want you to go through a function.
# So the error checking is in a function.
# Now, if a programmer, EVER, writes student.house in their code,
# then Python will not let the programmer access student.house directly.
# The instance variable, self.house, will auto call the setter function for me.

# It's the line
student.house = "Number Four, Privet Drive"
# in main, where house is the name of the setter/getter, and then the equals sign,
# that indicates to python, it's a visual clue, to say:
# wait a minute, I'm not going to let you access that attribute directly.
# I'm going to use the setter instead.
# Why? Because the = sign means I'm trying to a set a value to that attribute.

# And so I've also gotten rid of the code from the __init__ function that does the check
# Because in __init__ we've already got self.house = house
# meaning 'self.house ='  will take place and call the setter to do the error check.

# However I can't have instance variables named house AND methods called house
# They will collide, I need to decide
# Conventional fix is to have the setter not store the value passed in in self.house,
# But to use an almost identifical name, with an indicator you are doing this.
# you put an underscore in front of the instance variables name.
# So technically my instance variable is called _house
# And my property, which is a fancier attribute, if you will, is called house.

