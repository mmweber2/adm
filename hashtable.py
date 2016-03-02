# Empty object for use when deleting an object from the hash table.
class Placeholder(object):
  pass
# These placeholders don't need to be unique, can't I just make one?

class Item(object):
  # key = None
  # value = None

  def __init__(self, key, value):
    self.key = key
    self.value = value
  
class Table(object):
  # Total number of items currently in the hash table.
  items = 0
  # Non-empty spaces, including placeholders, in the hash table.
  spaces_filled = 0
  array = None
  INIT_SIZE = 10

  # Remember to check for half-full array and resize when adding.

  def __init__(self):
    self.array = [None for _ in xrange(self.INIT_SIZE)]

  def insert(self, key, value):
    # The length of the array will start as INIT_SIZE, but grow with the array.
    hashval = hash(key) % len(self.array)
    # First, check whether key already exists.
    # Don't add or change anything else if we just updated an existing key.
    if self._update_key(hashval, key, value):
      return
    # Spot is already full, with dummy or real value
    if self.array[hashval] is not None:
      hashval = _open_address(key, value, hashval + 1)
    # Once a spot is found, the item is going in the bucket and counts increment
    self.array[hashval] = Item(key, value)
    self.spaces_filled += 1
    self.items += 1
    if self.spaces_filled > len(self.array) / 2:
      resize()

  def _update_key(self, hashval, key, value):
    while hashval < len(self.array):
      if self.array[hashval] is None:
        return False
      # Key is already in the table, so overwrite it without changing any sizes.
      if self.array[hashval].key == key:
        self.array[hashval].value = value
        return True
      hashval += 1
    # Cycle back and check beginning of array.
    return _update_key(self, 0, key, value)

  # Bucket already has a dummy or valid key/value pair, so find a new bucket.
  def _open_address(self, hashval):
    while hashval < len(self.array):
      # New hash value found.
      if self.array[hashval] is None:
        return hashval
      hashval += 1
      # Reached end of array before finding an open space; start at the front.
      # It may seem that this would only happen if the hash is very full,
      #   but it's possible for an item to hash near the end of the array.
      return _open_address(self, 0)


# Hash key.
# Check if bucket is empty: if yes, add it.
# Check next buckets.
# If bucket has placeholder, keep going to make sure it's not there.
# Repeat from 2 onward.

