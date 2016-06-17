from multiply import multiply
from nose.tools import assert_equals

def test_multiply_small_numbers():
    assert_equals(multiply(2, 3), 6)

def test_multiply_different_lengths():
    assert_equals(multiply(1012, 35), 35420)

def test_multiply_zeroes():
    assert_equals(multiply(0, 10), 0)
    assert_equals(multiply(0, 0), 0)
    assert_equals(multiply(5, 0), 0)

def test_multiply_two_negative():
    assert_equals(multiply(-5, -3), 15)

# TODO: Test both numbers are negative
# Test either number is negative
# Test one number is really large



