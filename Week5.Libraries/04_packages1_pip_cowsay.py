# packages

# Packages are modules in folders, not just a file
# Packages are generally third-party libraries to install locally

# The PYPI website - Python package index. pypi.org

#### cowsay ###

# make a cow say something on your screen

# pypi.org/project/cowsay
# Too complex to download zip, extract, put in right place
# So most languages have a package manager.
# Python has pip

# So use
# pip install cowsay
# in the terminal

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1]) # cowsay.cow only takes 1 argument
else:
    print("wrong input")
# or could use cowsay.trex()

# Why is using sys.argv helpful to us?
# Well it's tedium to get asked again and again stuff if we are familiar with what the programme wants
# and we just put the input in right away instead.
# And If we want to rerun programmes as well, we want to just press up on our keyboard
# to find the last time we typed the whole thing
