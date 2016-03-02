import hashtable
from nose.tools import assert_raises

def setup():
  return hashtable.Table()

def test_lookup_empty():
  t = setup()
  assert_raises(KeyError, t.lookup, 2)

def test_lookup_absent():
  t = setup()
  t.insert(2, 0)
  assert_raises(KeyError, t.lookup, 0)

# Test lookup when deleted

# Also tests lookup, but has been tested separately as well.
def test_insert_one():
  t = setup()
  t.insert(5, 0)
  assert t.lookup(5) == 0
  assert t.items == 1
  assert t.spaces_filled == 1

def test_insert_collision():
  t = setup()
  t.insert(5, 0)
  t.insert(105, 2)
  assert t.items == 2
  assert t.spaces_filled == 2
  assert t.lookup(105) == 2

def test_insert_last():
  t = setup()
  t.insert(9, 5)
  assert t.lookup(9) == 5
  assert t.items == 1
  assert t.spaces_filled == 1

def test_insert_last_with_collision():
  t = setup()
  t.insert(9, 5)
  t.insert(109, 2)
  assert t.lookup(109) == 2
  assert t.items == 2
  assert t.spaces_filled == 2

def test_insert_replace():
  t = setup()
  t.insert(9, 5)
  t.insert(9, 0)
  assert t.lookup(9) == 0
  assert t.items == 1
  assert t.spaces_filled == 1

def test_insert_resize():
  t = setup()
  for i in xrange(6):
    t.insert(i, 0)
  assert t.lookup(1) == 0
  assert t.items == 6
  assert t.spaces_filled == 6

# None and empty strings are allowed as keys because they're part of an Item, 
#  so it will be different from the None showing a blank space.
def test_insert_none():
  t = setup()
  t.insert(None, 1)
  assert t.lookup(None) == 1

def test_insert_empty():
  t = setup()
  t.insert("", 1)
  assert t.lookup("") == 1

def test_delete_absent():
  t = setup()
  assert_raises(KeyError, t.delete, None) 

def test_delete_present():
  t = setup()
  t.insert(1, 10)
  assert t.lookup(1) == 10
  assert t.items == 1
  assert t.spaces_filled == 1
  t.delete(1)
  assert_raises(KeyError, t.lookup, 1)
  assert t.items == 0
  assert t.spaces_filled == 1

def test_insert_deleted():
  t = setup()
  t.insert(1, 10)
  t.delete(1)
  t.insert(1, 15)
  assert t.lookup(1) == 15
  assert t.items == 1
  assert t.spaces_filled == 2

