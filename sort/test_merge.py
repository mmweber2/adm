from merge import merge_sort
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


