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
    q = BoundedQueue(5.0)

def test_insert_first():
    q = BoundedQueue(2)
    q.insert(1, "test")
    node = q.array[1]
    assert q.array == [None, node, None]
    assert node.key == 1
    assert node.value == "test"

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
    pass

def test_find_min():
    pass

def test_find_min_empty():
    pass

def test_extract_min():
    pass

    # TODO: Try key, value
