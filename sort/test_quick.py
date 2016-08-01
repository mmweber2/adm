from quick import quicksort
from quick import _median_of_three as median
from random import sample
from nose.tools import assert_equals

def test_quick_empty():
    array = []
    quicksort(array)
    expected = []
    assert_equals(array, expected)

def test_quick_one():
    array = [1]
    quicksort(array)
    expected = [1]
    assert_equals(array, expected)

def test_quick_two():
    array = [2, 1]
    quicksort(array)
    expected = [1, 2]
    assert_equals(array, expected)

def test_quick_three():
    array = ["c", "d", "a"]
    quicksort(array)
    expected = ["a", "c", "d"]
    assert_equals(array, expected)

def test_quick_backwards():
    array = [4, 3, 2, 1]
    quicksort(array)
    expected = [1, 2, 3, 4]
    assert_equals(array, expected)

def test_quick_duplicates():
    array = [1, 4, 1, 3, 2, 4]
    quicksort(array)
    expected = [1, 1, 2, 3, 4, 4]
    assert_equals(array, expected)

def test_quick_large():
    array = sample(xrange(100000), 90)
    expected = sorted(array)
    quicksort(array)
    assert_equals(array, expected)

# Test _median_of_three
def test_median_in_order():
    seq = [2, 4, 6]
    assert_equals(median(seq), 4)
    assert_equals(seq, [2, 4, 6])

def test_median_reverse_order():
    seq = [3, 2, 1]
    assert_equals(median(seq), 2)
    assert_equals(seq, [1, 2, 3])

def test_median_median_at_zero_sorted():
    seq = [5, 0, 8]
    assert_equals(median(seq), 5)
    assert_equals(seq, [0, 5, 8])

def test_median_median_at_zero_backwards():
    seq = [2, 3, 1]
    assert_equals(median(seq), 2)
    assert_equals(seq, [1, 2, 3])

def test_median_median_at_end():
    seq = [2, -2, 1]
    assert_equals(median(seq), 1)
    assert_equals(seq, [-2, 1, 2])

def test_median_more_than_three():
    # 2 or 3 would be a valid median, so 3 (our mid index) is acceptable
    seq = [4, 5, 3, 1]
    assert_equals(median(seq), 3)
    # Remaining elements in list are left unsorted
    assert_equals(seq, [1, 5, 3, 4])

def test_median_duplicate():
    seq = [2, 2, 1]
    assert_equals(median(seq), 2)
    assert_equals(seq, [1, 2, 2])

def test_median_two():
    seq = [2, 1]
    # mid is index 1 (len is 2, divided by 2)
    assert_equals(median(seq), 2)
    assert_equals(seq, [1, 2])

def test_median_one():
    seq = [1]
    assert_equals(median(seq), 1)
    assert_equals(seq, [1])
