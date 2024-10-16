# Intro to re library

# We will use the most versatile function, re.search()

# re.search(pattern, string, flags=0)
#       pattern - what pattern we're looking for
#       string - where we are looking for the pattern
#       flags - lots of different flags to modify the behaviour of the function

import re

email = input("What's your email? ").strip()

# Now we've started off no better than our previous first script.
if re.search("@", email):
    print("Valid1")
else:
    print("Invalid1")

# We need more vocab. I want:
# something to the left, an @ sign, something in middle, period, something at right
# The pattern we pass to re.search() accepts a whole bunch of special symbols
#   .       any character except a new line
#   *       0 or more repetitions
#   +       1 or more repetitions
#   .+      1 or more of any character (except new line)
#   ..*     This would be the same as above, 1 or more any character
#   ?       0 or 1 repetitions
#   {m}     m repetitions
#   {m,n}   Between m and n repetitions

if re.search(".+@.+", email):
    print("Valid2")
else:
    print("Invalid2")

# Now a little bit about how re.search() is working in the computer.
# It uses a finite state machine, or more formally a nondeterminisistc finite automaton.
# re.search() begins in a start state.
# It reads from left to right and decides whether to stay in the first state,
# or transition to the next. As it reads patrick@cardiff.com against .*@.* it will compare
# p against .
# then a against .
# then t against .
# and so on, looping in that state,
# then it will transition when it reads @ and moves to the next state,
# then loop through the letters
# At the end of the function, the computer will check, did it end in the final accept state?
# If it did then it was a valid email address.
# If it finished in any other place it would reject the email address
# David showed all this graphically, but I can't.

# Now we still need to check for ".com" at the end?
# But how? How can we add'.com' when the period means any character?
# We use the 'escape character' which is backslash \
# We learned this when using new line characters \n
# so \. means we want to match an exact .

# But we also want to make sure that python treats the string as a raw string
# by putting r outside of the string to say don't treat any back slashes in the usual way
# But to pass \.com to the re.search() function.
# It's similar to use using the f at the beginning of a format string, telling python
# how to format a string, plugging in variables between curly braces
# But in this case r represents a raw string, where I want it passed in exactly as is.

if re.search(r".+@.+\.com", email):
    print("Valid3")
else:
    print("Invalid3")

# the r for raw string is not necessary unless backslashes are used,
# but it's good practice to always do it.

# Also 'my email address is patrick@cardiff.com' will be considered as valid
# let's solve that by introducing a few more symbols

#   ^       match the start of the string
#   $       match the end of the string (or just before the new line at the end)

if re.search(r"^.+@.+\.com$", email):
    print("Valid4")
else:
    print("Invalid4")

# But... 'patrick@@@@.com' is still valid
# So let's introduce more regular expression syntax
#   []      set of characters
#   [abc]   a, b or c
#   [a-z]   lower case alphabetical
#   [A-Z]   upper case alphabetical
#   [0-9]   all decimal
#   \d      all decimal, same as above
#   \s      white space characters
#   \w      all alphanumeric (and underscore), same as [a-zA-Z0-9_]
#   [^]     opposite of this set of characters (the complement)
#   [^@]    anything but an @ sign
# So let's replace the .+ with a [^@]+
# So that the strings either side do not contain @

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid5")
else:
    print("Invalid5")

# We're still being too accomodating though by saying usernames only exclude @
# What about other characters?
# Let's use the syntax above

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid6")
else:
    print("Invalid6")

# Or better yet, let's use \w to make it shorter
if re.search(r"^\w+@\w+\.com$", email):
    print("Valid7")
else:
    print("Invalid7")

# And also:
#   \D      not a decimal character
#   \S      not a white space character
#   \W      not a word (alphanumeric and underscore) character

# And if we wanted .com or .org we could end with this:
# \.(com|org|gov|net)
#   A|B         A or B
#   (...)       a group
#   (?:...)     non-capturing version

# But we can't be yelling our email, like PATRICK@CARDIFF.COM
# Because we're asking for .com in lower case, so .COM would be rejected
# We could just turn the input to lower case using .lower()
# But instead, let's learn about flags, because remember:
# re.search(pattern, string, flags=0)

####### re.search Flags ######

# Here are some flag examples for re.search()
# re.IGNORECASE     ignore the case of the users input
# re.MULTILINE      match multiple lines if paragraph provided
# re.DOTALL         so that . means any character including new lines
# These are sort of built in variables that have meaning for re.search

# I could now input PATRICK@CARDIFF.COM and it will be accepted
# but I haven't changed the value of the variable itself
if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE):
    print("Valid8")
else:
    print("Invalid8")

# But we have one more issue: patrick@cardiff.ac.com won't be accepted
# Because I'm not expecting any . character until .com
# there could be emails with several extra dots
# so if (...) groups things together let's use that.
# Because it wouldn't work if I replaced:
# r"^\w+@\w+\.com$"
# with:
# r"^\w+@\w+\.\w+\.com$"
# Because then it will accept @cardiff.ac.com, but not @cardiff.com
# so let's specify that part of this is optional
# We could do so with the pipe | character
# or with the '?' character which means 0 or 1 repetitions
# so let's add in (\w+\.)?  between the @ and the \w+\.com

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid9")
else:
    print("Invalid9")

# The actual OFFICIAL regular expression used by different websites is so complex
# It's really long, and you wouldn't want to type it all out manually
# But that's where our good friend libraries comes in.
# We don't need to define email addresses or website addresses, someone else has

########### Other functions in the re library ##########

# re.match(pattern, string, flags=0)
# Wery similar to re.search() but you don't need ^ to say match the beginning,
# re.match() will do that by design to automatically start matching at the start.

# re.fullmatch(pattern, string, flags=0)
# Similar to re.match(), but will match from start and end without ^ or $


