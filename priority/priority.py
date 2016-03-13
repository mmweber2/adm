import heap

class Queue(object):
  self.heap = Heap()

  # TODO: What should the queue pop if it's empty?
  def pop(self):
      """Returns the smallest item in the queue.
      """
      return self.heap.pop()

  def push(self, value):
      """Adds an item to the queue."""
      self.heap.push(value)
