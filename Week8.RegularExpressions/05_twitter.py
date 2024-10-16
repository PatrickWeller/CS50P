# twitter.py
# The aim of this file is to prompy users for the URL of their twitter profile,
# Then extract from it the user name
# A URL may look like https://twitter.com/patrickweller
url = input("URL: ").strip()

# This would find and replace, then leave the username
username = url.replace("https://twitter.com/","")
print(f"Username: {username}")
# We could use something like username = url.removeprefix("https://twitter.com/")
# But that would handle it differently if I said "my user name is https://....."

# But there are so many issues with this, it's too simple. Think about:
# https vs http vs no http
# twitter.com/username/hayas7af?va7=80?/
# www.twitter.com
# etc.

# let's use regular expressions to express the appropriate patterns we want
import re

##### Introducing re.sub() #####
# For susbtituting/replacing

# re.sub(pattern, repl, string, count=0, flags=0)
# pattern   The pattern to look for
# repl      What to replace that pattern with
# string    Where you look for that pattern
# count     how many times you find and replace
# flags     flags like earlier.

username = re.sub(r"https://twitter.com/","",url)
# This is no better than last time really
# AND we have a '.' in twitter.com!
# Meaning any character! so twitterQcom would be accepted
# Always be on the lookout for these sorts of characters
# So let's put a backslash before .
# and also a ? after the https so http is accepted
username = re.sub(r"https?://twitter\.com/","",url)
# and a carat ^ to say start like this
username = re.sub(r"^https?://twitter\.com/","",url)
# Now let's account for www. being there or not
username = re.sub(r"^https?://(www\.)?twitter\.com/","",url)
# And now what if the https/http isn't there?
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username: {username}")
# We've now got options within options (x?x)?
# We could even have parentheses within parentheses
# Regular syntax can get complex, but the syntax is always the same
# Just take baby steps, check at each step, and you won't go wrong
# Don't make a long regex in one go, do it incrementally


# Now let's go back to re.search() where we began to still incorporate some conditional
# element to our code, checking that at least something has been inputted right.
# Or else re.sub() will allow the user to put www.google.com/patrick and it will accept it.
# But we will move to the next script



