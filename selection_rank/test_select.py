from select import get_rank
import random
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_rank_empty():
    # Could return None or raise IndexError, but it will return None first.
    assert_equals(get_rank([], 0), None)

def test_rank_single_valid():
    assert_equals(get_rank([1], 0), 1)

def test_rank_negative_k():
    assert_raises(IndexError, get_rank, [1], -1)

def test_rank_too_large_k():
    assert_raises(IndexError, get_rank, [1, 2], 2)

def test_rank_smallest_of_three():
    array = [3, 1, 2]
    assert_equals(get_rank(array, 0), 1)

def test_rank_median_of_three():
    array = [2, 3, 1]
    assert_equals(get_rank(array, 1), 2)
    
def test_rank_largest_of_three():
    array = [1, 2, 3]
    assert_equals(get_rank(array, 2), 3)

def test_rank_duplicates():
    array = [1, 2, 3, 1, 2, 4, 2]
    assert_equals(get_rank(array, 2), 2)

def test_rank_sorted():
    array = [1, 3, 5, 7, 8, 9, 11, 13, 15, 20, 25, 30, 101, 116]
    assert_equals(get_rank(array, 2), 5)

def test_rank_large_unsorted():
    array = random.sample(xrange(10000), 80)
    assert_equals(get_rank(array, 30), sorted(array)[30])





