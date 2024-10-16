# Floats in testing

# We have to make room for approximation or tolerance when dealing with floats.
# There's only a finite number of bits to store each number
# But in reality floats can be very very long.
# We will consider 1.00000001 as 1.

# let's say we have a file that is converting values in AU to metres.
# in a test file we might used this

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691)

# We can adjust the tolernace like so
def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
# This means the convert function can give me this number, + or - 0.1
# could even do abs=1e-5
# We may be doing scientific work and need it to be very precise
# 1e-2 may be too low.
# adjust the tolerance to what you want
# then adjust the code to create what you want. 
