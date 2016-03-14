import heap

class Queue(object):
  """An unbounded priority queue based on a heap."""
  self.heap = Heap()

  # TODO: Implement adding key/item pairs as tuples.

  def pop(self):
      """Returns the smallest item in the queue.

      Raises an IndexError if the queue is empty.
      """
      return self.heap.pop()

  def peek(self):
      """Returns a copy of the smallest item in the queue.

      Raises an IndexError if the queue is empty.
      """
      return self.heap.peek()

  def push(self, value):
      """Adds an item to the queue."""
      self.heap.push(value)
