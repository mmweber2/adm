# Dictionary: set of n records, each with one or more key fields
# Build and maintain a data structure to efficiently locate, insert,
#  and delete the record associated with any query key q.

# We could make objects for this, but it is probably less memory to
#  just put the key/record pair in a list. If we weren't going to be
#  changing the record, we could use a tuple instead. 

# Unsorted list implementation
class Dic(object):
  items = None

  def __init__(self):
    self.items = []

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
    return self.items[loc][1]

  # Insert key q with value value.
  # If q is already in the dictionary, its value is overwritten.
  def insert(self, q, value):
    loc = self._locate(q)
    # q is already in the dictionary; overwrite it.
    if loc is not None:
      self.items[loc][1] = value
    # q is not in the dictionary
    else:
      self.items.append([q, value])

  # Delete does not return the value associated with the key.
  def delete(self, q):
    loc = self._locate(q)
    if loc is None:
      raise KeyError("Key {} not found in dictionary".format(q))
    self.items = self.items[:loc] + self.items[loc+1:]

