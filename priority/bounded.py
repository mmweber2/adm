class BoundedNode(object):
    """A Node to represent a single data point in the Queue."""
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next_item = None

class BoundedQueue(object):
    """A bounded-height priority queue."""

    def __init__(self, limit):
        """Creates a new BoundedQueue for priorities in the range 1 to
        limit, where limit is an integer >= 2.

        Raises a ValueError if limit is not an integer, or a IndexError
        if limit is less than 2.
        """
        if not isinstance(limit, int):
            raise ValueError("limit must be an integer.")
        if limit < 2:
          raise IndexError("limit must be greater than 1.")
        self._top = limit
        self._item_count = 0
        # Add an extra (blank) element to allow for 1-indexing.
        self.array = [None] * (limit + 1)

    def size(self):
        """Returns the maximum allowed priority for this Queue; valid
        priorities range from 1 to this number.

        Note that this is not the same as the number of items in
        the Queue; len() should be used for that.
        """
        return len(self.array) - 1

    def __len__(self):
        """Returns the number of items currently in the Queue."""
        return self._item_count

    def insert(self, priority, data):
        """Insert a piece of data into the queue with the given
        priority.

        Raises a TypeError if priority is not an integer, or an
        IndexError if 0 >= priority > limit. This limit was defined
        when the Queue was created.
        """
        if not isinstance(priority, int):
            raise TypeError(("priority is not an integer; it must be an" +
                " integer between 1 and limit."))
        # The array length check is not strictly necessary, but
        # it allows for a more specific error message.
        if not len(self.array) + 1 > priority >= 1:
            raise IndexError(("priority must be an integer between 1" +
                " and limit (inclusive)."
                ))
        # This node is the first for this priority.
        if self.array[priority] == None:
            self.array[priority] = BoundedNode(priority, data)
            self._top = min(self._top, priority)
        # This node is part of a chain for this priority.
        else:
            current = self.array[priority]
            # Add the new node to the top of the chain.
            self.array[priority] = BoundedNode(priority, data)
            self.array[priority].next_item = current
        self._item_count += 1

    def find_min(self):
        """Return the smallest item (the data associated with the
        smallest priority) in the Queue without removing it.

        If there are multiple items with the minimum priority, an
        unspecified item of that priority will be returned.

        Raises an IndexError if the Queue is empty.
        """
        if len(self) == 0:
            raise IndexError("Queue is empty.")
        return self.array[self._top].data

    def extract_min(self):
        """Returns and removes the smallest item (the data associated
        with the smallest priority) in the Queue.

        If there are multiple items with the minimum priority, the
        items will be returned in unspecified order.

        Raises an IndexError if the Queue is empty.
        """
        # Use find_min's error checking and get the data.
        data = self.find_min()
        node = self.array[self._top]
        # Min node has a next_item, so _top is unaffected.
        if node.next_item is not None:
            self.array[self._top] = node.next_item
        #_top needs to be incremented to next non-empty priority
        else:
            previous_top = self._top
            # Check for another non-empty priority location. There cannot
            # be another node before this one, because _top is always
            # compared to the new priority when inserting.
            # TODO: Use a stack to keep track of minimums so we do
            # not have to traverse up the full queue each removal.
            for i in xrange(previous_top + 1, self.size()):
                if self.array[i] is not None:
                    self._top = i
                    break
            # We did not find a successor to _top, so the last node in
            # the Queue was removed. Set._top to the last possible valid
            # data so that it will be properly updated if another data
            # is added.
            if self._top == previous_top:
                self._top = self.size()
        self._item_count -= 1
        return data
