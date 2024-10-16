# Constants - variables that no one can change
# It's a good part of coding defensively.

# Any time you hard code something, define it near the top of your code instead.
# And capitalise them!
# There's nothing actually stopping someone in python from changing it,
# It's all an honor system.
MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# Instead of:
for _ in range(3):
    print("meow")


####
# Remember class variables, variables that aren't inside self, per se.
# But are accessible to all methods inside that class.

# You can have class constants. So Class variables, capitalised, that should not be changed.
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

