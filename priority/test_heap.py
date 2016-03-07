from heap import Heap

def test_new():
    a = Heap()
    assert a.size == 0
    assert a.heap_list == [0]

def test_insert_first():
    a = Heap()
    a.insert(2)
    assert a.size == 1
    assert a.heap_list == [0, 2]

def test_insert_increasing():
    a = Heap()
    a.insert(2)
    a.insert(4)
    assert a.size == 2
    assert a.heap_list == [0, 2, 4]

def test_insert_decreasing():
    a = Heap()
    a.insert(4)
    a.insert(2)
    assert a.size == 2
    assert a.heap_list == [0, 2, 4]

def test_insert_multiple_heapify():
    a = Heap()
    a.insert(2)
    a.insert(4)
    a.insert(3)
    a.insert(1)
    assert a.size == 4
    assert a.heap_list == [0, 1, 2, 3, 4]

#TODO: Test adding duplicate numbers

#TODO: Test adding multiple variable/object types (shouldn't work).
