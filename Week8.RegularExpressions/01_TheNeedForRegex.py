# Intro to Regular Expressions

# Regexes are just patterns that you use to match to some data
# We need to define the pattern, then compare it and validate it,
# and we might then reject it or clean it up

# Let's say we want to validate an email address
# Let's start by just rejecting it if there's no @ symbol
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid1")
else:
    print("Invalid1")

# But this will says '@' is valid
# What if we incorporate a period as well?
if "@" in email and "." in email:
    print("Valid2")
else:
    print("Invalid2")

# Better, but '@.' would still be accepted, and so too ".@"
# Let's add a bit more logic.
username, domain = email.split("@")

# 'if username' returns true if there is at least one character in username
# You don't need the brackets here, but they are for readability for us learning
if (username) and ("." in domain):
    print("Valid3")
else:
    print("Invalid3")

# Let's get better, what if we want the email to end with ".ac.uk"
if (username) and (domain.endswith(".ac.uk")):
    print("Valid3")
else:
    print("Invalid3")

# But I could submit "patrick@.ac.uk" at this point which is still not good enough
# But this gets so complex and we have to write a lot of code for something quite simple really

######### re ############
# There is a library called re in python that will help us define patterns and validate inputs
# or even use the pattern to change the users input
# documentation is at docs.python.org/3/library/re.html

