# We've been using classes and objects all along though!

# Remember int? For integers
# Well look at
# docs.python.org/3/library/functions.html#int
# And you'll realise int was a class the whole time!
# This is the constructor call for an int

# class int(x, base=10)

# And we were being returned objects, of type int.
# Everytime we converted a string to an int, we've been creating an int object

# str has also been a class.
# docs.python.org/3/library/stdtypes.html#str
# Below is the constructor call

# class str(object='')

# We've been using str objects
# And any time we've forced a string to be lowercase per str.lower()
# We've been calling a method called lower,
# a method the authors of python built into the str class,

# str.strip([chars]) is another method inside the str class.
# and instances of strings have been objects the whole time.

# lists! They are classes too, with constructor call:
# class list([iterable])
# and list.append(x) has been a method in that list class

# dict is a class, we've been manipulating dict objects!

# The type function tells us the type of a variable
print(type(50)) # returns <class 'int'>
print(type("words")) # returns <class 'str'>
print(type(0.5)) # returns <class 'float'>
print(type(True)) # returns <class 'bool'>
print(type([])) # returns <class 'list'>
print(type(list())) # returns <class 'list'>
print(type({})) # returns <class 'dict'>
print(type(dict())) # returns <class 'dict'>
# Note, the default python classes start lower case
# When we make classes, our convention is starting with a capital
