from bounded import BoundedQueue
from bounded import BoundedNode
from nose.tools import assert_raises

def test_create_valid():
    q = BoundedQueue(2)

def test_create_one():
    assert_raises(IndexError, BoundedQueue, 1)

def test_create_string():
    assert_raises(ValueError, BoundedQueue, "test")

def test_create_float_whole():
    q = BoundedQueue(5.0)
    assert q.size() == 5

def test_create_float_trailing():
    q = BoundedQueue(2.5)
    assert q.size() == 2

def test_insert_first():
    q = BoundedQueue(2)
    q.insert(1, "test")
    node = q.array[1]
    assert q.array == [None, node, None]
    assert node.key == 1
    assert node.value == "test"

def test_insert_maximum_key():
    q = BoundedQueue(2)
    q.insert(2, "max")
    node = q.array[2]
    assert node.key == 2
    assert node.value == "max"

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
    node = q.array[1]
    assert node.key == 1
    assert node.value == "test"
    child = node.child
    assert child.key == 1
    assert child.value == "again"

def test_insert_not_collision():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(2, "again")
    node = q.array[2]
    assert node.key == 2
    assert node.value == "again"

def test_find_min_single_item():
    q = BoundedQueue(3)
    q.insert(1, "test")
    value = q.find_min()
    assert value == "test"

def test_find_min_multiple_keys():
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(2, "again")
    value = q.find_min()
    assert value == "test"

def test_find_min_key_chain():
    """Find_min should not be sorting the values within a key."""
    q = BoundedQueue(3)
    q.insert(1, "test")
    q.insert(1, "again")
    value = q.find_min()
    assert value == "test"

def test_find_min_empty():
    q = BoundedQueue(2)
    assert_raises(IndexError, q.find_min)

def test_extract_min():
    pass

