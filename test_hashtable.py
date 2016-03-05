import hashtable
import mock
import __builtin__
from nose.tools import assert_raises

def test_lookup_empty():
  t = hashtable.Table()
  assert_raises(KeyError, t.lookup, 2)

def test_lookup_absent():
  t = hashtable.Table()
  t.insert(2, "test")
  assert_raises(KeyError, t.lookup, "test")

def test_insert_one():
  t = hashtable.Table(10)
  t.insert(5, "test")
  assert t.lookup(5) == "test"
  assert len(t) == 1
  assert t.spaces_filled == 1
  assert t.array[5].key == 5
  assert t.array[5].value == "test"

@mock.patch('__builtin__.hash', return_value=2)
def test_insert_collision(mock_hash):
  t = hashtable.Table(10)
  t.insert(5, "test")
  t.insert(10, "test again")
  assert mock_hash.call_count == 2
  assert len(t) == 2
  assert t.spaces_filled == 2
  assert t.lookup(5) == "test"
  assert t.lookup(10) == "test again"
  assert mock_hash.call_count == 4
  assert t.array[2].key == 5
  assert t.array[3].key == 10

def test_insert_last():
  t = hashtable.Table(5)
  t.insert(4, "test")
  assert t.lookup(4) == "test"
  assert len(t) == 1
  assert t.spaces_filled == 1

@mock.patch('__builtin__.hash', return_value=2)
def test_insert_last_with_collision(mock_collision):
  # Fake hash returns 2
  t = hashtable.Table(3)
  t.insert(9, "test")
  t.insert(10, "test again")
  assert t.lookup(9) == "test"
  assert t.lookup(10) == "test again"
  assert len(t) == 2
  assert t.spaces_filled == 2

def test_insert_replace():
  t = hashtable.Table()
  t.insert(9, 5)
  t.insert(9, "test")
  assert t.lookup(9) == "test"
  assert len(t) == 1
  assert t.spaces_filled == 1

@mock.patch('__builtin__.hash', return_value=2)
def test_insert_replace_with_collision(mock_collision):
  t = hashtable.Table(5)
  t.insert(9, "test")
  t.insert(10, "test again")
  t.insert(9, "test this instead")
  assert t.lookup(9) == "test this instead"
  assert t.lookup(10) == "test again"
  assert len(t) == 2
  assert t.spaces_filled == 2

def test_insert_resize():
  t = hashtable.Table(3)
  t.insert("cheese", "cake")
  t.insert("birthday", "party")
  assert t.lookup("cheese") == "cake"
  assert len(t) == 2
  assert t.spaces_filled == 2
  assert len(t.array) == 6

# None and empty strings are allowed as keys because they're part of an Item, 
#  so it will be different from the None showing a blank space.
def test_insert_none():
  t = hashtable.Table()
  t.insert(None, 1)
  assert t.lookup(None) == 1

def test_insert_empty():
  t = hashtable.Table()
  t.insert("", 1)
  assert t.lookup("") == 1

def test_delete_absent():
  t = hashtable.Table()
  assert_raises(KeyError, t.delete, "taste") 

def test_delete_present():
  t = hashtable.Table()
  t.insert(1, 10)
  assert t.lookup(1) == 10
  assert len(t) == 1
  assert t.spaces_filled == 1
  t.delete(1)
  assert_raises(KeyError, t.lookup, 1)
  assert len(t) == 0
  assert t.spaces_filled == 1

def test_insert_deleted():
  t = hashtable.Table()
  t.insert(1, 10)
  t.delete(1)
  t.insert(1, 15)
  assert t.lookup(1) == 15
  assert len(t) == 1
  assert t.spaces_filled == 2

def test_delete_resize():
  t = hashtable.Table(10)
  for i in xrange(5):
    t.insert(i, "test")
  t.delete(2)
  t.delete(4)
  # Add 5 items and delete 2.
  assert len(t) == 3
  assert t.spaces_filled == 5
  assert len(t.array) == 10
  # Add 1 more item, pushing it over the resize point.
  t.insert(6, 1)
  assert t.lookup(3) == "test"
  assert len(t) == 4
  assert t.spaces_filled == 4
  assert len(t.array) == 20


