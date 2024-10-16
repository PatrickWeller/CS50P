############# class methods ###########

# Thus far we've used instance variables, and instance methods
# But there are other types of variables and methods.
# And one of those is class methods.

# Sometimes not necessary or sensible to associate functions with objects of a class,
# but rather the class itself.
# FUnctionality that is the same no matter the specific object's own values/instance variables are.

# @classmethod
# This is another decorator, another class method that DOES NOT have access to 'self'
# But it does know what class it's inside.

# Firstly, let's get some code.

# Sorting Hat
import random

class Hat:
    def __init__(self):
        # Kept in class, so can use for many methods in class
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

# Slightly weird though that in this short script we could do:
hat1 = Hat()
hat2 = Hat()
hat3 = Hat()
# and technically have more than one sorting hat.
# Often classes represent real world things, and in this case, there is just one sorting hat.
# I don't need to keep instantiating it.
# So how can we fix that?

# So until now we've just used instance methods:
# Writing functions inside classes that are automatically passed a reference to self, the current object.

# But sometimes you don't need that and it's enough to know wha tthe class is and assume that
# there might be no objects of that class.
# So a class can be a container - a container for data and/or functionality that is conceptionally related.


class Hat:
    # I don't need to instantiate multiple houses with init.
    # So let's get a class variable! So I no longer use self.houses, just houses.
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Passing in cls, not self, to mean pass in the own class, not the own object.
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# Not instantiating a hat object, just getting the class and it's method.
Hat.sort("Harry")

# So far this is relatively simple, we could have just done this with a function or two.
# But the code gets messy quickly
# These classes and classmethods will really help with organisation!


# Let's clean up student.py a bit further, making use of classmethods.
# Here is where we left it (minus the properties):

class Student:  # All student specific functionality should be bundled up here
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

# And it's this bit that is a missed opportunity to clean up our code.
# This function helps us get a student, their name and their house.
# I should be looking at the class Student for all Student functionality,
# So currently it's bad design.
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()



# Class methods mean we can address this.
class Student:  # All student specific functionality should be bundled up here
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

# We've made a class method called 'get' meaning we can call the function,
# without instantiating a Student object first. Helping solve the chicken and egg problem.
# So I can call Student.get before having a student object.
# The name is just 'get' because it's already associated with the student class,
# and can't be used otherwise.


# Static methods are also a thing, but we won't go down that rabbit hole!

