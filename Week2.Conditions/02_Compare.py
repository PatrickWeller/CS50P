# compare.py

x = int(input("What is x? "))
y = int(input("What is y? "))

# We want to make a decision based on the values of x and y
# Use if. Make sure you do the colon, and the indent.
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x ==y:
    print("x is equal to y")

# These are boolean expression. True or False answer.

# Currently though, regardless of the answer of question 1, the program has to ask all 3 questions
# We could improve it though, by introducing elif

# elif

# If we get a TRUE answer, we don't want to keep asking questions

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# We wouldn't notice a difference because it's a small code.
# But it's good practice before our code gets bigger.

# But if can be even better,
# There is no need to ask our 3rd and final question.
# if x isn't greater or isn't less than y, it's obviously equal
# so two lines can be

else:
    print("x is equal to y")


# OR

# We could ask a couple of questions at once with OR

x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Can improve it slightly if we are nitpicky
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

