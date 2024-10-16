# APIs and Requests

# APIs live on some other server, and we can communicate with them
# and submit and download data from them

##### requests
# the requests library let's us interact with APIs by making web requests
# Documentation is at
# pypi.org/project/requests

# so on the terminal run:
# pip install requests

### Itunes API ###

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer
# Made this by reading the itunes API documentation.
# So I'm asking for song information (not album or artist)
# limit of 1
# term equals weezer

# if I enter this on my browser then that will download a JSON file
# curly brace at start and end, square brackets too. Then a bunch of key-value pairs.
# Completely text based format, in a standardised way of all information in Apples database,
# regarding the first weezer song.

# now let's let our script and terminal act as a browser making a http request.

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# User can specify their band of choice
response = requests.get("https://itunes.apple.com/search?entity=song&limit=3&term=" + sys.argv[1])

# print(response.json())
# Python will return in the terminal a JSON response (JavaScript Object Notation),

# But the python requests library will convert it to a python dictionary
# Which has nearly the same syntax
    # curly braces for the dictionary
    # square braces for lists inside
    # single quotes for strings that are keys in teh dictionary
    # colons to then afterwards store the value of that key

# But guess what?
# Python also comes with a library called json allowing you to manipulate JSON data!
# it will make it way easier to understand by displaying it nicely.

import json

#print(json.dumps(response.json(),indent=2))

# So the dictionary has 2 keys resultCount of 1, and results with a value of a list of dictionaries,
# in this case, one dictionary

# And what if I just want the track name?
# Well I can do this:

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# And I can change the limit in the URL to get more song names
