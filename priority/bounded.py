class BoundedNode(object):
    """A Node to represent a single data point in the Queue."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.child = None

    def link(self, child):
        """Link another Node as the child (next node) of this Node."""
        self.child = child

class BoundedQueue(object):
    """A bounded-height priority queue."""

    def __init__(self, limit):
        """Creates a new BoundedQueue for keys in the range 1
        to limit, where limit is an integer >= 2.

        Raises a ValueError if limit is not an integer, or a IndexError
        if limit is less than 2.
        """
        if limit < 2:
          raise IndexError("limit must be greater than 1.")
        limit = int(limit)
        # Allow 1-indexing of the array.
        limit += 1
        self.array = [None] * limit
        self.top = limit

    def insert(self, key, value):
        """Insert a key, value pair into the queue.

         Raises a TypeError if key is not an integer, or a IndexError
         if key is not greater than 0 and less than or equal to limit,
         as defined when the queue was created.
         """
        # When an item is removed, top is incremented until it reaches a
        # non-empty list.

        # This is enclosed in a try/except because some invalid values
        # will result in different errors; for example, None raises a
        # TypeError and "test" raises a ValueError.
        try:
            # Like limit, key must be converted to an int for indexing.
            key = int(key)
        except ValueError:
            raise TypeError(
                "Key must be an integer between 1 and limit (inclusive)."
                )
        # The array length check is not strictly necessary, but
        #     it allows for a more specific error message.
        if key < 1 or key > len(self.array) + 1:
            raise IndexError(
                "Key must be an integer between 1 and limit (inclusive)."
                )
        # Make a new Node for this key.
        if self.array[key] == None:
            self.array[key] = BoundedNode(key, value)
            self.top = min(self.top, key)
        #TODO: If there's already a node there, child it.
