import heap

class Queue(object):
    """An unbounded priority queue based on a heap."""

    def __init__(self):
        """Creates a new, empty queue.

        Calling pop() or peek() before calling push() will raise an
        IndexError.
        """
        self.heap = heap.Heap()

    def pop(self):
        """Returns the value associated with the smallest key in the
        queue, and removes the key/value pair from the queue.

        Raises an IndexError if the queue is empty.
        """
        # We could just return pop()[1], but this allows us more
        #     flexibility later on and is easier to read.
        key, value = self.heap.pop()
        return value

    def peek(self):
        """Returns the value associated with the smallest key in the
        queue.

        Raises an IndexError if the queue is empty.
        """
        key, value = self.heap.peek()
        return value

    def push(self, key, value):
        """Adds an item to the queue."""
        self.heap.push((key, value))

    def size(self):
        """Returns the number of items in the queue.

        An empty queue is of size 0.
        """
        return self.heap.size()
