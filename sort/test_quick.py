from quick import quicksort
from nose.tools import assert_equals

def test_quick_empty():
    assert_equals(quicksort([]), [])

def test_quick_one():
    assert_equals(quicksort([1]), [1])

def test_quick_one_as_string():
    assert_equals(quicksort("a"), ["a"])

def test_quick_two():
    assert_equals(quicksort([2, 1]), [1, 2])

def test_quick_three():
    assert_equals(quicksort("cda"), ["a", "c", "d"])

def test_quick_backwards():
    assert_equals(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

def test_quick_duplicates():
    assert_equals(quicksort([1, 4, 1, 3, 2, 4]), [1, 1, 2, 3, 4, 4])


