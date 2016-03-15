from priority import Queue
from nose.tools import assert_raises

def test_push_and_peek():
  a = Queue()
  a.push(1, "test")
  assert a.peek() == "test"
  a.push(3, "test again")
  assert a.peek() == "test again"

def test_pop():
  a = Queue()
  a.push("string", "methods")
  a.push("are", "useful")
  assert a.pop() == "useful"
  assert a.pop() == "methods"

def test_peek_items_removed():
  a = Queue()
  a.push(3, "remove")
  a.pop()
  assert_raises(IndexError, a.peek)

def test_peek_ever_empty():
  a = Queue()
  assert_raises(IndexError, a.peek)
