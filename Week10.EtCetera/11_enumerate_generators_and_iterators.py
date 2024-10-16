##### enumerate, generators and iterators.

#### enumerate

# So we can tell us the position in the list of these students like this.
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

# Or instead of range(len()) we can use enumerate
# Gives you back both the index AND the value in one go.
students = ["Hermione", "Harry", "Ron"]
for i, student in enumerate(students):
    print(i + 1, student)


##### generators

# Computer may run out of memory is reading or generating lots of data.
# Let's count some sheep.
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)

if __name__ == "__main__":
    main()

# Well let's incorporate a sheep() function
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "🐑" * n

if __name__ == "__main__":
    main()

# But the main function is still doing the iteration.
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = [n]
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()

# But now if I try and run this with 1000000 sheep, then I've got an issue.
# Getting a little lost. But we do want the best practices,
# of having this helper function generating sheep.
# But we want to use generators now, to return just a little bit at a time,
# not all at once.

# We will use a new word:
# yield
# instead of return.

# Instead of building up a massive list of sheep in 'flock',
# let's do this:
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i # If we had return here, it wouldn't work.
                        # sheep(n) would stop as it returned a value.
                        # But yield hands one piece of data at a time.

if __name__ == "__main__":
    main()


# yield is returning an iterator.

