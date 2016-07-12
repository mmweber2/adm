from knapsack import knapsack
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_empty_items():
    assert_equals(knapsack([], 5), [])

def test_zero_capacity():
    assert_equals(knapsack([(1, 2), (2, 1)], 0), [])

def test_negative_capacity():
    assert_raises(IndexError, knapsack, [(1, 2), (2, 1)], -1)

def test_negative_size_item():
    assert_raises(IndexError, knapsack, [(-1, 2), (2, 1)], 3)

def test_single_item_fits():
    assert_equals(knapsack([(1, 1)], 1), [0])

# Tests to add:
# Non-zero capacity, but too small for any items
# Items with negative value
# Finds best choice when it can fit one of two items
# Finds two items better value than one large (non-greedy)
# Larger subsets
