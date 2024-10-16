########### Inheritance ##############

# Design your classes in a hierarchical fashion, so that they borrow attributes from higher classes

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

# Already we have some redudancy!
# Both classes have a name, and identical lines of code of self.name = name
# it would get even worse and repetitive if we add the code:
if not name:
    raise ValueError("Missing name")
# Because we would add that code to both!

# So let's add inheritance - define multiple classes that relate to each other in some way

# Students and Professors are BOTH wizards. So let's have a Wizard class that has a name!

class Wizard:
    def __init__(self, name):
        # Error checking of name only needs to be here once :)
        if not name:
            raise ValueError("Missing name")
        self.name = name

# When I define a Student class, inherit all the properties and functionality of Wizard class
class Student(Wizard):
    def __init__(self, name, house):
        # Inherit the parent class and access it's init method
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")
wizard = Wizard("Albus")

# Exceptions are hierarchical btw, a heirarchical class that inherits the features of the parent class.
# E.g.
BaseException
    KeyboardInterrupt
    Exception
        ArithmeticError
            ZeroDivisionError
        AssertionError
        etc.
# If you're not sure which error may be raised, just catch the parent/super class exception type.


