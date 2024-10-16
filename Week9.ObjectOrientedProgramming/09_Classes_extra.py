def main():
    packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]

main()

# This code is rubbish. Strings are too flexible, could easily be changed format-wise.
# Classes are like template.
# We could create a template of what packages look like.

# We want:
    # ID
    # Sender
    # Recipient
    # Weight

class Package:
    def __init__(self, id, sender, recipient, weight)
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return(f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg")

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
        Package(id=1, sender="Alice", recipient="Bob", weight=10),
        Package(id=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    for package in packages:
        print(f"{package} costs £{package.calculate_cost(cost_per_kg=2)}")

main()

# I've defined two instances of the Package class.
# Defined how they can be printed nicely
# And made an instance method for calculating cost.
