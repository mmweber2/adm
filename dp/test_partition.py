from partition import partition
from nose.tools import assert_equals
from nose.tools import assert_raises

#def test_partition_ten_1s():
#    seq = [1] * 10
#    assert_equals(partition(seq, 3), 3)
#    assert_equals(partition(seq, 1), 9)
#    assert_equals(partition(seq, 9), 1)
#
def test_partition_different_numbers():
    seq = [i for i in xrange(1, 10)]
    assert_equals(partition(seq, 3), 17)
#
#def test_partition_empty_seq():
#    assert_raises(IndexError, partition, [], 2)
#
#def test_partition_zero_k():
#    seq = [1, 2, 3]
#    assert_raises(IndexError, partition, seq, 0)
