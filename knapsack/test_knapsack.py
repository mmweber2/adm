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
    assert_equals(knapsack([(1, 1)], 1), [(1, 1)])

def test_single_item_too_big():
    assert_equals(knapsack([(2, 2)], 1), [])

def test_negative_value():
    assert_equals(knapsack([(2, -3)], 2), [])

def test_size_greater_than_value():
    assert_equals(knapsack([(5, 2)], 7), [(5, 2)])

def test_value_greater_than_size():
    assert_equals(knapsack([(2, 5)], 3), [(2, 5)])

def test_too_small_capacity():
    assert_equals(knapsack([(2, 3)], 1), [])

def test_best_of_two_choices():
    assert_equals(knapsack([(2, 1), (2, 2)], 2), [(2, 2)])

# Tests to add:

# Doesn't try to fit the same item more than once
# Finds two items better value than one large (non-greedy)
# Larger subsets
