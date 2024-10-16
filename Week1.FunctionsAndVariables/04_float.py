# Dealing with floats now, numbers with decimal points
x = float(input("What's X? "))
y = float(input("What's Y? "))

print(x + y)

# What if we want to round the final value to the nearest integer?
# Here is it's syntax
# round(number[, ndigits)
# The [ means that what follows is optional
# You can pass in 1 to round to 1 digit after the point, or 2 to round 2 digits after the point.
# e.g. tenths or hundreths.

z = round(x + y)

print(z)

# If we want to include commas for big numbers we can bring back the f string

print(f"{z:,}")

# On to Division
A = float(input("What's A? "))
B = float(input("What's B? "))

#can round to 2 decimal places
C = round(A/B, 2)
print(C)

#Can use f variable again and this is the weird syntax for it
print(f"{C:.2f}")
