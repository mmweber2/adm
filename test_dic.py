# Test file for dictionary programs.

import dic
from nose.tools import assert_raises

# These test methods are somewhat dependent on each other; for example, we 
#   have to use test_locate in order to see if test_insert worked.

def test_locate_single():
  active_dict = dic.Dic()
  active_dict.insert('a', 0)
  assert active_dict.locate('a') == 0

def test_locate_multiple():
  active_dict = dic.Dic()
  active_dict.insert('a', 0)
  active_dict.insert('c', 2)
  active_dict.insert('b', 1)
  assert active_dict.locate('c') == 2

def test_locate_empty():
  active_dict = dic.Dic()
  assert_raises(KeyError, active_dict.locate, 'a')

def test_insert():
  pass

def test_delete():
  pass
