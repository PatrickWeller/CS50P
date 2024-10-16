# Intro to unit tests

# Quite common to not just write your code, but to write a little extra code to test the code you wrote.
# So that's what we will do, write our own test.


# I have a file calculator.py which will square an input number

# I can't test infinite numbers of course,
# But i need to test more than just 2 and 3. But 0, negative numbers, etc.

# In the file I've readied it to call main conditionally,
# so that I can safely import one or more things from the file into another file

# My testing file will be called test_calculator.py
# Look at it.
# I've set it up to import the square function from my calculator.py
# then test 2 numbers and tell me if the output is wrong
# I'll get nothing if it's all right

# The issue is I've now got more lines of code for my test than i do my calculator.
# And really I want to test more cases.



#### assert ####

# Can assert, boldly claim something is true!
# If it's acutally not true, then you'll get a boolean error.
# Use this in my new test_calculator2.py

# I can break my calculator for a bit by changing n * n to n + n to see things go wrong
# It will say AssertionError in the terminal when one of my assertions is false.
# Unless i try to catch an AssertionError and explain it with try and except
# But this adds more lines of code once again!
# And I once again want to try negatives and 0 etc.

#### pytest ####

# pytest is a third party program to automate code testing.
# It adopts conventions so you don't need to write as many lines of code yourself to test manually
# Note: Some unit testing programs come with python by default, but David argues pytest is simpler

# Unit testing - testing individual units, usually functions, that you have written.

# test_calculator3.py is now a much smaller test bit of code, without try and except etc.
# without the main functional either, no prints. Very simple.
# but pytest can still tell me what goes wrong.
# run this

pip install pytest
pytest test_calculator3.py

# Will give me a slightly difficult output.
# Will show me in red what's going wrong
# It tells me that I'm trying to assert that 6 = 9, which it doesn't.
# So I can go back and figure out why square(3) is equalling 6.
# if it's all OK it will give me a dot and say 100% and be in green :)

# At the moment our test isn't testing the main function of the calculator, only the square function.
# A user could put in a float or a string etc. and we aren't testing for that.
# But this is one of the reasons we separate our code into functions.
# So we can test each part individually.

# But we can improve upon our test_calculator3.py even more!
# As it stands in that test file, when something goes wrong,
# it only tells us the first error. It doesn't run all the tests.
# It would be good to know all of them that will fail.
# That gives us the best chance of us knowing why they failed and saves time

# so test_calculator4.py
# I've separated test_square() in my test into 3 different tests:
# test_positive, test_negative, and test_zero
# Each will run and I'll get to see errors from each.

# And now below the 3 mathematical tests I'll also just test the users input too
# if they input 'cat' which is not a number, i want it to work OK in producing an TypeError.
# so I import pytest
# then use the code:
# def test_str():
#    with pytest.raises(TypeError):
#        square("cat")
