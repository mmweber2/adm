from longest_inc_seq import longest_increasing_sequence as lis
from nose.tools import assert_equals

def test_empty_sequence():
    assert_equals(lis([]), [])

def test_sequence_of_one():
    assert_equals(lis([5]), [5])

def test_sequence_ascending_order():
    seq = [1, 2, 3, 4]
    assert_equals(lis(seq), seq)

def test_sequence_descending_order():
    seq = [3, 2, 1]
    assert_equals(len(lis(seq)), 1)

def test_sequence_mixed_order():
    seq = [1, 2, 9, 3, 4]
    assert_equals(lis(seq), [1, 2, 3, 4])

def test_sequence_mixed_multiple():
    seq = [2, 4, 3, 5, 1, 7, 6, 9, 8]
    assert_equals(len(lis(seq)), 5)


