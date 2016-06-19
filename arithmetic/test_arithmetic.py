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
    assert_equals(multiply(0, -5), 0)

def test_multiply_two_negative():
    assert_equals(multiply(-5, -3), 15)
    assert_equals(multiply(-2, 3), -6)
    assert_equals(multiply(2, -1), -2)

def test_multiply_large():
    # 2**64 is just beyond the bounds of int, so Python makes it a long
    assert_equals(multiply(2**64, 100), 1844674407370955161600)



