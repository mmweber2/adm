import hashtable

def setup():
  return hashtable.Table()

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



# Test insert with resizing
# Test lookup when empty
# Test lookup when absent
# Test insert over a placeholder

