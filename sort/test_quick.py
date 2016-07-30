from quick import quicksort
from quick import _median_of_three as median
from random import sample
from nose.tools import assert_equals

def test_quick_empty():
    assert_equals(quicksort([]), [])

def test_quick_one():
    assert_equals(quicksort([1]), [1])

def test_quick_two():
    assert_equals(quicksort([2, 1]), [1, 2])

def test_quick_three():
    assert_equals(quicksort(["c", "d", "a"]), ["a", "c", "d"])

def test_quick_backwards():
    assert_equals(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

def test_quick_duplicates():
    assert_equals(quicksort([1, 4, 1, 3, 2, 4]), [1, 1, 2, 3, 4, 4])

def test_quick_large():
    input_list = sample(xrange(100000), 10)
    assert_equals(quicksort(input_list), sorted(input_list))

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
