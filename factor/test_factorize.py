from factorize import factorize
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_negative():
    assert_raises(ValueError, factorize, -1)

def test_zero():
    assert_raises(ValueError, factorize, 0)

def test_one():
    assert_raises(ValueError, factorize, 1)

def test_two():
    assert_equals(factorize(2), [2])

def test_prime():
    assert_equals(factorize(5), [5])

def test_single_factor():
    assert_equals(factorize(9), [3, 3])

def test_multi_factor():
    assert_equals(factorize(21), [3, 7])

def test_multi_factor_repeats():
    assert_equals(factorize(147), [3, 7, 7])

def test_cubed():
    assert_equals(factorize(27), [3, 3, 3])

def test_larger_prime():
    assert_equals(factorize(13), [13])
