############# Operator Overloading ############

# Can take very simple syntax like + and - and implement our own interpretation of it.

# Vault.py

class Vault:
    # Can pass in values, but default values is zero
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# How would I combine the funds of both potter and weasley?
# I could do:
# galleons = potter.galleons + weasley.galleons
# etc.
# Then
# total = Vault(galleons, sickles, knuts)
# print(total)
# But this is a lot of effort
# What if I could just do potter + weasley

# We can OVERRIDE the + operator to make it do what we want.

# See special-method-names in the documentation.
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# object.__add__(self, other)
# self is on the left of a plus sign
# other is on the right of a plus sign.

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."


    # New method that overrides + when using two vaults!
    # As long as the operand on the left of the + is a vault, you can actually add anything on the right
    # But they might not have a galleons value, so you would change the code below...
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
