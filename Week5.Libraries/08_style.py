# Style!

# Style is subjective, but the community has tried to codify style in PEP8

# consistency as an individual is important
# consistency within a project is more importnat
# consistency within one module or function is most important

# Consider:
# Indentation
# Tabs or Spaces (4 spaces is reccomended)
# Maximum line length
# Blank lines
# Imports

# Reading the guide and comparing our code with it is a bit lame and tedious
# So there are tools to helps us

### linters - e.g. pylint

# Analyses your code and tries to figure out if any consistency mistakes
# pip install pylint

# pylint can be noisy though, will find so many issues!
# so how about we use
# pycodestyle
# pip install pycodestyle
# pycodestyle.pycqa.org
# it will just fix it for you!

# or how about
# black
# pip install black
# black.readthedocs.io

# just run it with:
# black file.py

# Can focus more now on writing good logical code, and let black make it look pretty.
