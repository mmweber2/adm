from bounded import BoundedQueue
from bounded import BoundedNode
from nose.tools import assert_raises

def test_create_valid():
    q = BoundedQueue(2)

def test_create_one():
    assert_raises(IndexError, BoundedQueue(1))

def test_create_string():
    assert_raises(ValueError, BoundedQueue("test"))

def test_create_float():
    q = BoundedQueue(5.0)

def test_insert():
    # TODO: Try key, value

  """When the set of keys is {1, 2, ..., C}, and only insert, 
  find-min and extract-min are needed, a bounded height priority
  queue can be constructed as an array of C linked lists plus a pointer top,
  initially C. Inserting an item with key k appends the item to the k'th,
  and updates top ← min(top, k), both in constant time. Extract-min deletes and
  returns one item from the list with index top, then increments top if needed 
  until it again points to a non-empty list; this takes O(C) time in the worst case""".
