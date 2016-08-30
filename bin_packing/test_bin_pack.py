from nose.tools import assert_equals
from nose.tools import assert_raises
from bin_packing import bin_pack
import math
import random

def test_item_sizes_empty():
    assert_equals(bin_pack([], 5), 0)

def test_item_sizes_with_string():
    assert_raises(ValueError, bin_pack, [3, "3"], 5)

def test_item_sizes_with_None():
    assert_raises(ValueError, bin_pack, [None], 5)

def test_negative_item_size():
    assert_raises(ValueError, bin_pack, [1, -2, 3], 3)

def test_item_size_too_big():
    assert_raises(ValueError, bin_pack, [1, 2, 3], 2)

def test_zero_capacity():
    assert_raises(ValueError, bin_pack, [1, 2, 3], 0)

def test_non_number_capacity():
    assert_raises(TypeError, bin_pack, [1, 2], "3")

def test_fill_single_box_one_item():
    assert_equals(bin_pack([2], 2), 1)

def test_same_size_items_ints():
    assert_equals(bin_pack([5, 5, 5, 5], 6), 4)

def test_same_size_items_floats():
    assert_equals(bin_pack([.1 for _ in xrange(10)], 1.0), 1)

def test_fill_single_box_multiple_items():
    assert_equals(bin_pack([2, 1, 2], 5), 1)

def test_irregular_capacity():
    assert_equals(bin_pack([2, 1, 2], math.pi), 2)

def test_large():
    for _ in xrange(100):
        sizes = range(1, 51)
        assert_equals(bin_pack(sizes, 50), 26)
