# We want to reformat the user's input in the format we expect

# Someone might input there name as 'David Malan', or 'Malan, David'
# Unlikely, but maybe.
# And if I used if statements initially in my form, I could have rejected this.
# But I forgot, and now I'm left cleaning up the data I've already got.
# Imagine instead of asking for input above, I'm reading a csv file

# The below code could clean up some of this data
# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

# But someone could be sloppy and submit 'Malan,David' with no space
# So I want to split on ", ?" to mean there could be 0 or 1 spaces
# Unfortuantely split doesn't have built in functionality with regex syntax.

# Before we just used re.search to say true or false, now we want to capture info from it.
# We can use parenthesis to capture and return information from re.search()
# (...)     a grroup, but also capture this info
# (?:...)   a group but non-capturing version

# In the code below I want to capture the first and last name,
# so I've put parentheses around those bits, the .+ bits.
# It will put that data in matches
# And i've accounted for there maybe not being a space after a comma, using ', ?'
import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)

# So now I can ask a Boolean question, if there are matches, then print.
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")
# If my input is 'Patrick Weller', then the if statement does nothing,
# and it prints my own inputted name.
# But if there is a comma it will do the if statement.

# And a neater way perhaps of doing it.
# Note there is something else in index zero for these groups!
# A convention of
if matches:
    name = matches.groups(2) + " " + matches.group(1)
print(f"Hello, {name}")

# Well we can tighten things up even further! See next file.
