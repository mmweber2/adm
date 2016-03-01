# Dictionary: set of n records, each with one or more key fields
# Build and maintain a data structure to efficiently locate, insert,
#  and delete the record associated with any query key q.

# We could make objects for this, but it is probably less memory to
#  just put the key/record pair in a list. If we weren't going to be
#  changing the record, we could use a tuple instead. 

# Unsorted list implementation
class Dic(object):
  # Since Python lists are flexible, we don't need to track n separately.
  items = None
  # For quick checking of whether or where an item exists in the dictionary.
  itemset = None

  def __init__(self):
    self.items = []
    self.itemset = set()

  # Locate key q in the dictionary and return its value.
  # Raises a KeyError if q is not in the dictionary.
  def locate(self, q):
    # Make sure q is in the set before scanning everything
     _check_for_key(q)
    for item in self.items:
      if item[0] == q:
        return item[1]

  # Insert key q with value value.
  # If q is already in the dictionary, its value is overwritten.
  def insert(self, q, value):
    # q is already in the dictionary
    if q in self.itemset:
      for item in self.items:
        if item[0] == q:
          item[1] = value
    # q is not in the dictionary
    else:
      self.items.append([q, value])
      self.itemset.add(q)

  def delete(self, q):
    _check_for_key(q)
    self.itemset.remove(q)
    for i in xrange(len(self.items)):
      if self.items[i][0] == q:
        self.items[i] = None
        return
    
  def _check_for_key(self, q):
    if q not in self.itemset:
      raise KeyError("Key {} not found in dictionary".format(q))



