from merge import merge_sort
from random import sample
from nose.tools import assert_equals

def test_merge_empty():
    assert_equals(merge_sort([]), [])

def test_merge_one():
    assert_equals(merge_sort([1]), [1])

def test_merge_two():
    assert_equals(merge_sort([2, 1]), [1, 2])

def test_merge_three():
    assert_equals(merge_sort(["c", "d", "a"]), ["a", "c", "d"])

def test_merge_backwards():
    assert_equals(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

def test_merge_duplicates():
    assert_equals(merge_sort([1, 4, 1, 3, 2, 4]), [1, 1, 2, 3, 4, 4])

# Sample does not create duplicates, but we've already confirmed that
# the sort handles duplicates in the previous test.
def test_merge_large():
    input_list = sample(xrange(100000), 90)
    assert_equals(merge_sort(input_list), sorted(input_list))


