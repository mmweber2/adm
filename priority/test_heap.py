from heap import Heap
from nose.tools import assert_raises

def test_new():
    a = Heap()
    assert a.size == 0
    assert a.heap_list == [0]

def test_push_first():
    a = Heap()
    a.push(2)
    assert a.size == 1
    assert a.heap_list == [0, 2]

def test_push_increasing():
    a = Heap()
    a.push(2)
    a.push(4)
    assert a.size == 2
    assert a.heap_list == [0, 2, 4]

def test_push_decreasing():
    a = Heap()
    a.push(4)
    a.push(2)
    assert a.size == 2
    assert a.heap_list == [0, 2, 4]

def test_push_multiple_heapify():
    a = Heap()
    a.push(2)
    a.push(4)
    a.push(3)
    a.push(1)
    assert a.size == 4
    assert a.heap_list == [0, 1, 2, 3, 4]

def test_push_duplicates():
    a = Heap()
    a.push(5)
    a.push(7)
    a.push(5)
    assert a.size == 3
    assert a.heap_list == [0, 5, 7, 5]

def test_push_zero():
    a = Heap()
    a.push(2)
    a.push(3)
    a.push(0)
    assert a.size == 3
    assert a.heap_list == [0, 0, 3, 2]

def test_push_negative():
    a = Heap()
    a.push(-1)
    assert a.size == 1
    assert a.heap_list == [0, -1]

def test_pop_empty():
    a = Heap()
    assert_raises(IndexError, a.pop)

def test_pop_one():
    a = Heap()
    a.push(1)
    assert a.pop() == 1
    assert a.size == 0
    assert a.heap_list == [0]

def test_pop_three():
    a = Heap()
    a.push(1)
    a.push(-1)
    a.push(2)
    assert a.pop() == -1
    assert a.size == 2
    assert a.heap_list == [0, 1, 2]

def test_pop_three_levels():
    a = Heap()
    a.push(5)
    a.push(9)
    a.push(11)
    a.push(14)
    a.push(18)
    assert a.pop() == 5
    assert a.size == 4
    assert a.heap_list == [0, 9, 14, 11, 18]

#TODO: Test adding multiple variable/object types (shouldn't work).
