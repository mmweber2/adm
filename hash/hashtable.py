from collections import namedtuple

Item = namedtuple('Item', ['key', 'value'])

class Table(object):
  INIT_SIZE = 10
  RESIZE_RATIO  = .5

 def __init__(self, size=INIT_SIZE):
    self.array = [None] * size
    # Total number of items currently in the hash table.
    self.items = 0
    # Non-empty spaces, including placeholders, in the hash table.
    self.spaces_filled = 0

  # Length of dictionary is considered to be the number of items in it, not
  #   the number of spaces filled or slots available.
  def __len__(self):
    return self.items

  @staticmethod
  def _hashit(key, array_size):
    # I currently use the built in hash(), but I'm moving it here in case
    #   I want to change the hash function later on.
    return hash(key) % array_size

  def insert(self, key, value):
    """If the key hashes to an available value, stores it there.
    If the key hashes the same as a previously used value, stores it in
    the next available space, looping around the end.
    If the key is already in the dictionary, it's overwritten.
    (There is no check for whether the value is the same.)
    The length of the array will start as INIT_SIZE, but grow with the array.
    """
    hashval = Table._hashit(key, len(self.array))
    # First, check whether key already exists.
    # Don't add or change anything else if we just updated an existing key.
    if self._update_key(hashval, key, value):
      return
    # Spot is already full, with dummy or real value
    if self.array[hashval] is not None:
      hashval = Table._open_address(hashval + 1, self.array)
    # Once a spot is found, the item is going in the spot and counts increment
    self.array[hashval] = Item(key, value)
    self.spaces_filled += 1
    self.items += 1
    if float(self.spaces_filled)/ len(self.array) > self.RESIZE_RATIO:
      self._resize()

  def lookup(self, key):
    hashval = Table._hashit(key, len(self.array))
    index = self._get_lookup_index(hashval, key)
    if index is None:
      raise KeyError("Key \"{}\" not found.".format(key))
    return self.array[index].value

  def _get_lookup_index(self, hashval, key):
     """ Find the index of a key in array, if it exists.
     Returns None if it doesn't exist.
     """
    while True:
      # Cycle back and check beginning of array. This won't result in a full
      # loop because we'll have to hit a None before looping through
      # the array, since it is no more than half full.
      if hashval == len(self.array):
        hashval = 0
      current_item = self.array[hashval]
      # Key is not in array.
      if current_item is None:
        return None
      # A valid item is in the bucket
      if type(current_item) is Item:
        if current_item.key == key:
          return hashval
      hashval += 1

  def delete(self, key):
    hashval = Table._hashit(key, len(self.array))
    index = self._get_lookup_index(hashval, key)
    if index is None:
      raise KeyError("Key \"{}\" not found.".format(key))
    self.array[index] = ""
    self.items -= 1

  def _update_key(self, hashval, key, val):
    index = self._get_lookup_index(hashval, key)
    # Key is not already in dictionary.
    if index is None:
      return False
    # Key is already in the table, so overwrite it without changing any sizes.
    self.array[hashval] = self.array[hashval]._replace(value=val)
    return True

  def _resize(self):
    new_size = len(self.array) * 2
    new_array = [None] * new_size
    for current_item in self.array:
      if type(current_item) is Item:
        hashval = Table._hashit(current_item.key, new_size)
        if new_array[hashval] is not None:
          hashval = Table._open_address(hashval, new_array)
        # Don't increment the size, because that was already done for this item
        new_array[hashval] = current_item
    # All placeholders have been removed, so it is now full of real items.
    self.spaces_filled = self.items
    self.array = new_array

  # index already has a dummy or valid key/value pair, so find a new index.
  @staticmethod
  def _open_address(hashval, array):
    while True:
      # Reached end of array before finding an open space; start at the front.
      # It may seem that this would only happen if the hash is very full,
      #   but it's possible for an item to hash near the end of the array.
      if hashval == len(array):
        hashval = 0
      # New hash value found.
      if array[hashval] is None:
        return hashval
      hashval += 1
