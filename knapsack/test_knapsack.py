from knapsack import knapsack
from nose.tools import assert_equals

def test_empty_items():
    assert_equals(knapsack([], 5), [])

def test_zero_capacity():
    assert_equals(knapsack([(1, 2), (2, 1)], 0), [])

# Tests to add:
# 0 capacity
# Negative capacity
# Non-zero capacity, but too small for any items
# Fits single item
# Finds best choice when it can fit one of two items
# Finds two items better value than one large (non-greedy)
# Larger subsets
