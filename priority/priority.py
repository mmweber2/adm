import heap

class Queue(object):
    """An unbounded priority queue based on a heap."""

    # TODO: Implement adding key/item pairs as tuples.

    def __init__(self):
        """Creates a new, empty queue.

        Calling pop() or peek() before push() will raise an IndexError.
        """
        self.heap = heap.Heap()

    def pop(self):
        """Returns the value associated with the smallest key in the
        queue, and removes the key/value pair from the queue.

        Raises an IndexError if the queue is empty.
        """
        return self.heapq.pop()

    def peek(self):
        """Returns the value associated with the smallest key in the
        queue.

        Raises an IndexError if the queue is empty.
        """
        return self.heapq.peek()

    def push(self, value):
        """Adds an item to the queue."""
        self.heapq.push(value)
