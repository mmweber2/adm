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

         Raises a ValueError if limit is not an integer, or
         an IndexError if limit is less than 2.
         """
         if limit < 2:
           raise IndexError("limit must be greater than 1.")
         self.array = [None] * limit
         # Todo: Test key for validity (int >1 and < limit)
