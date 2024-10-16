# We can clean up our script even more
# See how we define matches, then say if matches on the next line?
# What if that could be on the same line?
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    name = matches.groups(2) + " " + matches.group(1)
print(f"Hello, {name}")

# See how we can just condense those 2 lines with  'if' ':=' and ':'
# We use this only if you want to assign something from right to left AND ask an if question.
# := is known as the walrus operator
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.groups(2) + " " + matches.group(1)
print(f"Hello, {name}")
