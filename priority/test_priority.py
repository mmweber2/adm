from priority import Queue
from nose.tools import assert_raises

def test_push_multiple():
    a = Queue()
    assert a.size() == 0
    a.push(1, "test")
    a.push(3, "test again")
    assert a.peek() == "test"
    assert a.size() == 2

def test_push_new_min():
    a = Queue()
    a.push(1, "test")
    a.push(3, "test again")
    a.push(-1, "keep testing")
    assert a.peek() == "keep testing"
    assert a.size() == 3

def test_size_after_peek():
    a = Queue()
    a.push(1, "test")
    assert a.size() == 1
    assert a.peek() == "test"
    assert a.size() == 1

def test_pop():
    a = Queue()
    a.push("string", "methods")
    a.push("are", "useful")
    assert a.pop() == "useful"
    assert a.size() == 1
    assert a.pop() == "methods"
    assert a.size() == 0

def test_peek_items_removed():
    a = Queue()
    a.push(3, "remove")
    a.pop()
    assert_raises(IndexError, a.peek)

def test_peek_ever_empty():
    a = Queue()
    assert_raises(IndexError, a.peek)
