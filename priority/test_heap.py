from heap import Heap
from nose.tools import assert_raises

def test_new():
    a = Heap()
    assert a.size() == 0
    assert a.heap_list == [0]

def test_push_first():
    a = Heap()
    a.push(2)
    assert a.size() == 1
    assert a.peek() == 2

def test_peek():
    """Other functions test the ordering of the elements elsewhere,
    so I'm only testing peek once.
    """
    a = Heap()
    a.push(3)
    assert a.peek() == 3
    assert a.size() == 1
    # Element has not been removed
    assert a.peek() == 3

def test_push_increasing():
    a = Heap()
    a.push(2)
    a.push(4)
    assert a.size() == 2
    assert a.pop() == 2
    assert a.pop() == 4

def test_push_decreasing():
    a = Heap()
    a.push(4)
    a.push(2)
    assert a.size() == 2
    assert a.pop() == 2
    assert a.pop() == 4

def test_push_out_of_order():
    """Prove that the heap_list isn't just sorting the values."""
    a = Heap()
    a.push(4)
    a.push(2)
    a.push(3)
    assert a.size() == 3
    assert a.heap_list == [0, 2, 4, 3]

def test_push_multiple_heapify():
    a = Heap()
    a.push(2)
    a.push(4)
    a.push(3)
    a.push(1)
    assert a.size() == 4
    assert a.pop() == 1
    assert a.pop() == 2
    assert a.pop() == 3
    assert a.pop() == 4

def test_push_duplicates():
    a = Heap()
    a.push(5)
    a.push(7)
    a.push(5)
    assert a.size() == 3
    assert a.pop() == 5
    assert a.pop() == 5
    assert a.pop() == 7

def test_push_zero():
    a = Heap()
    a.push(0)
    assert a.size() == 1
    assert a.pop() == 0

def test_push_negative():
    """Prove that the 0 at index 0 won't get in the way of
       keys that compare as less than 0.
    """
    a = Heap()
    a.push(-1)
    assert a.size() == 1
    assert a.pop() == -1

def test_pop_empty():
    a = Heap()
    assert_raises(IndexError, a.pop)

def test_pop_one():
    a = Heap()
    a.push(1)
    assert a.pop() == 1
    assert a.size() == 0
    assert_raises(IndexError, a.pop)

def test_pop_three():
    a = Heap()
    a.push(1)
    a.push(-1)
    a.push(2)
    assert a.pop() == -1
    assert a.size() == 2
    assert a.pop() == 1
    assert a.pop() == 2

def test_pop_three_levels():
    a = Heap()
    a.push(5)
    a.push(9)
    a.push(11)
    a.push(14)
    a.push(18)
    assert a.pop() == 5
    assert a.size() == 4
    assert a.heap_list == [0, 9, 14, 11, 18]

def test_min_child():
    a = Heap()
    a.push(5)
    a.push(11)
    a.push(9)
    a.push(14)
    a.push(18)
    assert a.pop() == 5
    assert a.heap_list == [0, 9, 11, 18, 14]

def test_push_multiple_types():
    """Assuming implementation where 2 < 'strings'."""
    a = Heap()
    a.push(2)
    a.push('strings')
    assert a.pop() == 2
    assert a.pop() == 'strings'

