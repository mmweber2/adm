# Test file for dictionary programs.

import self_dic
from nose.tools import assert_raises

# These test methods are somewhat dependent on each other; for example, we 
#   have to use test_locate in order to see if test_insert worked.

def setup():
  return self_dic.SelfDic()

def test_locate_single():
  active_dict = setup()
  active_dict.insert('a', 0)
  assert active_dict.locate('a') == 0

def test_locate_multiple():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.insert('c', 2)
  active_dict.insert('b', 1)
  assert active_dict.locate('c') == 2

def test_locate_empty():
  active_dict = setup()
  assert_raises(KeyError, active_dict.locate, 'a')

def test_locate_multiple_not_present():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.insert('c', 2)
  active_dict.insert('b', 1)
  assert_raises(KeyError, active_dict.locate, 'd')

def test_insert_empty():
  active_dict = setup()
  active_dict.insert('a', 0)
  assert active_dict.locate('a') == 0

def test_insert_multiple():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.insert('c', 3)
  active_dict.insert('b', 1)
  assert active_dict.locate('c') == 3

def test_insert_duplicate():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.insert('c', 3)
  active_dict.insert('a', 1)
  assert active_dict.locate('a') == 1

def test_delete_absent():
  active_dict = setup()
  active_dict.insert('a', 0)
  assert_raises(KeyError, active_dict.delete, 'd')

def test_delete_present():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.delete('a')
  # Searching for a deleted key should now give a KeyError.
  assert_raises(KeyError, active_dict.locate, 'a')

def test_delete_deleted():
  active_dict = setup()
  active_dict.insert('a', 0)
  active_dict.delete('a')
  # Trying to delete an already deleted key should give a KeyError.
  assert_raises(KeyError, active_dict.delete, 'a')
