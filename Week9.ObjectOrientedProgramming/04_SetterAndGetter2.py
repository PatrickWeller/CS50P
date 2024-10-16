# We will now add a setter and getter to name
# We've already added a setter and getter to house

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

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
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# Now we have error checking for both name and house,
# two variables we expect might be changed over the course of their use.
# But of course, we could act adversarially and still mess it up.
# In our main function, we could use the following code:
# student.house = "Dumstrang"
# And we know that wouldn't work as '.house =' will go through the setter
# But what if we used the following code in our main function:
# student._house = "Dumstrang"
# The property is called house, but the instance variable is called _house

# In the world of python it's the honor system
# if you see an instance variable starting underscore, then don't touch it
# It's signifies it should be private, don't touch it
# and sometimes programmers use double underscore (dunder) to mean REALLY don't touch it.
# But there's nothing actually stopping us. Python let's us change them.
# Java does not allow us ever in contrast.



