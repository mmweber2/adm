from collections import namedtuple

# Empty object for use when deleting an object from the hash table.
class Placeholder(object):
  pass
# Instead of Placeholder, let's try using "".

Item = namedtuple('Item', ['key', 'value'])

class Table(object):
  # Total number of items currently in the hash table.
  items = 0
  # Non-empty spaces, including placeholders, in the hash table.
  spaces_filled = 0
  array = None
  INIT_SIZE = 10

  def __init__(self):
    self.array = [None for _ in xrange(self.INIT_SIZE)]

  # If the key hashes to an available value, stores it there.
  # If the key hashes to a previously used value, stores it in the next
  #   available space, looping around the end.
  # If the key is already in the dictionary, it's overwritten. 
  #   (There is no check for whether the value is the same.)
  def insert(self, key, value):
    # The length of the array will start as INIT_SIZE, but grow with the array.
    hashval = hash(key) % len(self.array)
    # First, check whether key already exists.
    # Don't add or change anything else if we just updated an existing key.
    if self._update_key(hashval, key, value):
      return
    # Spot is already full, with dummy or real value
    if self.array[hashval] is not None:
      hashval = self._open_address(hashval + 1, self.array)
    # Once a spot is found, the item is going in the bucket and counts increment
    self.array[hashval] = Item(key, value)
    self.spaces_filled += 1
    self.items += 1
    if self.spaces_filled > len(self.array) / 2:
      self.resize()

  def lookup(self, key, hashval=None):
    if hashval is None:
      hashval = hash(key) % len(self.array)
    while hashval < len(self.array):
      current_slot = self.array[hashval]
      if current_slot is None:
        raise KeyError("Key \"{}\" not found.".format(key))
      if type(current_slot) is Item:
        if current_slot.key == key:
          return current_slot.value
      # Slot is a Placeholder or has another key in it
        hashval += 1
    # Cycle back and check beginning of array.
    return self.lookup(key, 0)

  # Find the index of a key in array, if it exists.
  # Returns None if it doesn't exist, or KeyError if the key is invalid.
  @staticmethod
  def _get_lookup_index(key, array, hashval=None):
    if key is None or key is "":
      raise KeyError("Key {} is invalid.")
    if hashval is None:
      hashval = hash(key) % len(array)
    while hashval < len(array):
      current_bucket = array[hashval]
      # Key is not in array.
      if current_bucket is None:
        return None
      # A valid item is in the bucket
      if type(current_bucket) is Item:
        if current_bucket.key == key:
          return hashval
      hashval += 1
    # Cycle back and check beginning of array.
    return Table._get_lookup_index(key, array, 0)

  def delete(self, key):
    pass

  def _update_key(self, hashval, key, val):
    index = Table._get_lookup_index(key, self.array)
    # Key is not already in dictionary.
    if index is None:
      return False
    # Key's index was found. 
    # Key is already in the table, so overwrite it without changing any sizes.
    self.array[hashval] = self.array[hashval]._replace(value=val)
    return True

  def resize(self):
    new_size = len(self.array) * 2
    new_array = [None for _ in xrange(new_size)]
    for bucket in self.array:
      if type(bucket) is Item:
        hashval = hash(bucket.key) % new_size
        if new_array[hashval] is not None:
          hashval = self.open_address(hashval, new_array)
        # Don't increment the size, because that was already done for this item
        new_array[hashval] = bucket
      if type(bucket) is Placeholder:
        self.spaces_filled -= 1

  # Bucket already has a dummy or valid key/value pair, so find a new bucket.
  def _open_address(self, hashval, array):
    while hashval < len(array):
      # New hash value found.
      if array[hashval] is None:
        return hashval
      hashval += 1
      # Reached end of array before finding an open space; start at the front.
      # It may seem that this would only happen if the hash is very full,
      #   but it's possible for an item to hash near the end of the array.
    return self._open_address(0, array)

# Hash key.
# Check if bucket is empty: if yes, add it.
# Check next buckets.
# If bucket has placeholder, keep going to make sure it's not there.
# Repeat from 2 onward.

