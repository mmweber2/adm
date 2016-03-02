# Dictionary: set of n records, each with one or more key fields
# Build and maintain a data structure to efficiently locate, insert,
#  and delete the record associated with any query key q.

# This will be a self-organizing dictionary that moves items when they
# are accessed or inserted.

# Unsorted list implementation
class SelfDic(object):
  items = None

  def __init__(self):
    self.items = []

  # Move the item with the given index to the front of the list.
  def _move(self, i):
    self.items = [self.items[i]] + self.items[:i] + self.items[i+1:]

  # Internal function to find key in dictionary.
  def _locate(self, q):
    for i in xrange(len(self.items)):
      if self.items[i][0] == q:
        return i

  # Locate key q in the dictionary and return its value.
  # Raises a KeyError if q is not in the dictionary.
  def locate(self, q):
    loc = self._locate(q)
    if loc == None:
      raise KeyError("Key {} not found in dictionary.".format(q))
    self._move(loc) 
    # Since the item has been accessed, it's now at the front of the list.
    return self.items[0][1]

  # Insert key q with value value.
  # If q is already in the dictionary, its value is overwritten.
  def insert(self, q, value):
    loc = self._locate(q)
    # q is already in the dictionary; overwrite it.
    if loc is not None:
      self._move(loc)
      self.items[0][1] = value
    # q is not in the dictionary
    else:
      self.items.append([q, value])
      # Take the newly added item and move it to the front.
      self._move(len(self.items) - 1)

  # Delete does not return the value associated with the key.
  def delete(self, q):
    loc = self._locate(q)
    if loc is None:
      raise KeyError("Key {} not found in dictionary".format(q))
    self.items = self.items[:loc] + self.items[loc+1:]

