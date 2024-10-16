#  Many tests

# Suppose we have many different tests and we want to start to organise them,
# maybe into multiple files or even a folder.
# pytests and other frameworks support us doing this
# So I've made a folder called "test"
# In this example I will only have one test file in there,
# but in reality I could have many.

# I have a file in there, test_hello.py
# to test my hello.py

# I then need to create one more file in that folder, called:
# __init__.py
# And even though this __init__.py is empty, it tells pytest to treat the folder as a package.
# A package is multiple modules organised in a folder.
# __init__.py is just a visual indicator for python to treat it that way.
# I can do more things with this file if more was in the folder, but we'll leave it empty for now.

# Can now run in the terminal@
pytest test
# to run pytest on all tests in that folder
