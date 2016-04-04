from bounded import BoundedQueue
from bounded import BoundedNode
from nose.tools import assert_raises

def test_create_valid():
    q = BoundedQueue(2)

def test_create_one():
    assert_raises(IndexError, BoundedQueue, 1)

def test_create_string():
    assert_raises(ValueError, BoundedQueue, "test")

def test_create_float():
    assert_raises(ValueError, BoundedQueue, "5.0")

def test_insert_first():
    q = BoundedQueue(2)
    q.insert(1, "test")
    node = q.array[1]
    assert q.array == [None, node, None]
    assert node.priority == 1
    assert node.data == "test"

def test_insert_maximum_priority():
    q = BoundedQueue(2)
    q.insert(2, "max")
    node = q.array[2]
    assert node.priority == 2
    assert node.data == "max"

def test_insert_invalid_int():
    q = BoundedQueue(2)
    assert_raises(IndexError, q.insert, 3, "test")

def test_insert_zero():
    q = BoundedQueue(2)
    assert_raises(IndexError, q.insert, 0, "test")

def test_insert_not_int():
    q = BoundedQueue(3)
    assert_raises(TypeError, q.insert, "test", "test now")

def test_insert_None():
    q = BoundedQueue(2)
    assert_raises(TypeError, q.insert, None, "never mind")

def test_insert_collision():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(1, "again")
    # Don't test on the order, since implementation may change.
    nodes = set((q.array[1].data, q.array[1].next_item.data))
    assert "test" in nodes
    assert "again" in nodes

def test_insert_not_collision():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(2, "again")
    node = q.array[2]
    assert node.priority == 2
    assert node.data == "again"

def test_find_min_single_item():
    q = BoundedQueue(3)
    q.insert(1, "test")
    data = q.find_min()
    assert data == "test"

def test_find_min_multiple_priorities():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(2, "again")
    data = q.find_min()
    assert data == "test"

def test_find_min_empty():
    q = BoundedQueue(2)
    assert_raises(IndexError, q.find_min)

def test_extract_min_standard():
    q = BoundedQueue(2)
    q.insert(2, "test")
    assert q.extract_min() == "test"
    assert len(q) == 0

def test_extract_min_same_priority():
    q = BoundedQueue(2)
    q.insert(2, "test")
    q.insert(2, "test two")
    nodes = set((q.extract_min(), q.extract_min()))
    assert "test" in nodes
    assert "test two" in nodes

def test_extract_min_different_priorities():
    q = BoundedQueue(4)
    q.insert(3, "test")
    q.insert(1, "testing")
    assert q.extract_min() == "testing"
    assert q.extract_min() == "test"

def test_insert_3_with_1_collision():
    q = BoundedQueue(3)
    q.insert(2, "test 1")
    q.insert(1, "test 2")
    q.insert(2, "test 3")
    assert q.extract_min() == "test 2"
    nodes = set((q.extract_min(), q.extract_min()))
    assert "test 1" in nodes
    assert "test 3" in nodes

def test_extract_min_empty():
    q = BoundedQueue(2)
    assert_raises(IndexError, q.extract_min)

def test_extract_min_already_removed():
    q = BoundedQueue(4)
    q.insert(3, "test")
    q.extract_min()
    assert_raises(IndexError, q.extract_min)

def test_len_empty():
    q = BoundedQueue(4)
    assert len(q) == 0

def test_len_single():
    q = BoundedQueue(3)
    q.insert(1, "test")
    assert len(q) == 1

def test_len_removed_one():
    q = BoundedQueue(3)
    q.insert(2, "test")
    q.extract_min()
    assert len(q) == 0

def test_len_collision():
    q = BoundedQueue(2)
    q.insert(1, "test")
    q.insert(1, "test again")
    assert len(q) == 2

def test_len_collision_removed():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(1, "test again")
    q.extract_min()
    assert len(q) == 1

