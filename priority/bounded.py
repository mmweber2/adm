class BoundedNode(object):
    """A Node to represent a single data point in the Queue."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.child = None

class BoundedQueue(object):
    """A bounded-height priority queue."""

    def __init__(self, limit):
        """Creates a new BoundedQueue for keys in the range 1 to limit,
        where limit is an integer >= 2.

        If limit is a floating point number, it will be rounded down to
        the nearest integer.

        Raises a ValueError if limit is not an integer, or a IndexError
        if limit is less than 2.
        """
        if limit < 2:
          raise IndexError("limit must be greater than 1.")
        limit = int(limit)
        self.top = limit
        self.item_count = 0
        # Allow 1-indexing of the array.
        limit += 1
        self.array = [None] * limit

    def size(self):
        """Returns the maximum allowed key value for this Queue; valid
        key values range from 1 to this value.

        Note that this is not the same as the number of items (inserted
        pairs) in the Queue.
        """
        return len(self.array) - 1

    def insert(self, key, value):
        """Insert a key, value pair into the queue.

         Raises a TypeError if key is not an integer, or a IndexError
         if key is not greater than 0 and less than or equal to limit,
         as defined when the queue was created.
         """
        # This is enclosed in a try/except because some invalid values
        # will result in different errors; for example, None raises a
        # TypeError and "test" raises a ValueError.
        try:
            # Like limit, key must be converted to an int for indexing.
            key = int(key)
        except ValueError:
            raise TypeError(
                ("Key must be an integer between 1 and {}" +
                "(inclusive).".format(self.size))
                )
        # The array length check is not strictly necessary, but
        # it allows for a more specific error message.
        if key < 1 or key > len(self.array) + 1:
            raise IndexError(
                "Key must be an integer between 1 and limit (inclusive)."
                )
        # This node is the first for this key.
        if self.array[key] == None:
            self.array[key] = BoundedNode(key, value)
            self.top = min(self.top, key)
        # This node is part of a chain for this key.
        else:
            current = self.array[key]
            while current.child is not None:
                current = current.child
            current.child = BoundedNode(key, value)
        self.item_count += 1

    def find_min(self):
        """Return the smallest item (the value associated with the
        smallest key) in the Queue without removing it.

        Raises an IndexError if the Queue is empty.
        """
        if self.item_count == 0:
            raise IndexError("Queue is empty.")
        return self.array[self.top].value

    def extract_min(self):
        """Returns and removes the smallest item (the value associated
        with the smallest key) in the Queue.

        Raises an IndexError if the Queue is empty.
        """
        # Use find_min's error checking and get the value.
        value = self.find_min()
        node = self.array[self.top]
        # Min node has a child, so top is unaffected.
        if node.child is not None:
            self.array[self.top] = node.child
        # Top needs to be incremented to next non-empty key
        else:
            previous_top = self.top
            # Check for another non-empty key location. There cannot
            # be another node before this one, because top is always
            # compared to the new key when inserting.
            for i in xrange(previous_top + 1, len(self.array)):
                if self.array[i] is not None:
                    self.top = i
                    break
            # We did not find a successor to top, so the last node in
            # the Queue was removed. Set top to the last possible valid
            # value so that it will be properly updated if another value
            # is added.
            if self.top == previous_top:
                self.top = self.size()
        self.item_count -= 1
        return value
