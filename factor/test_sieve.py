from sieve import sieve
from nose.tools import assert_raises
from nose.tools import assert_equals

def test_negative():
    assert_raises(ValueError, sieve, -3)

def test_zero():
    assert_raises(ValueError, sieve, 0)

def test_one():
    assert_raises(ValueError, sieve, 1)

def test_two():
    assert_equals(sieve(2), [2])

def test_three():
    assert_equals(sieve(3), [2, 3])

def test_four():
    assert_equals(sieve(4), [2, 3])

def test_larger_prime():
    assert_equals(sieve(13), [2, 3, 5, 7, 11, 13])

def test_larger_non_prime():
    assert_equals(sieve(14), [2, 3, 5, 7, 11, 13])

