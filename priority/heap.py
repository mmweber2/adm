class Heap(object):
    """A data structure of ordered keys with quick access to the
    smallest key in the set.

    The default comparator is used.
    """
    def __init__(self):
        # Start with a never-used 0 as index 0 for easy integer division,
        #     multiplication, and indexing.
        self.heap_list = [0]

    def push(self, value):
        """Add an item to the heap."""
        self.heap_list.append(value)
        self._heap_up()

    def size(self):
        """Returns the number of items in the Heap.
        A newly created Heap is of size 0.
        """
        return len(self.heap_list) - 1

    def peek(self):
        """Returns the smallest item in the Heap without altering it.

        Raises an IndexError if the Heap is empty.
        """
        if self.size() == 0:
          raise IndexError("No items on the heap.")
        return self.heap_list[1]

    def _heap_up(self):
        """For push; move a newly added value from the end of the
        array up to its proper index.
        """
        # Always start at the (newly added) last item of the array.
        index = self.size()
        # Checking for index / 2 > 0 means that we never alter the
        #    base 0 at index 0.
        while index / 2 > 0:
            if self.heap_list[index] < self.heap_list[index / 2]:
                self.heap_list[index], self.heap_list[index / 2] = (
                    self.heap_list[index / 2], self.heap_list[index])
            index /= 2

    def _heap_down(self):
        """For pop; move a newly swapped value down from the root to
        its proper index.
        """
        # Always start at the (newly changed) root.
        index = 1
        # Move down until the node doesn't have any children.
        while index * 2 <= self.size():
            smaller_child = self._min_child(index)
            if self.heap_list[index] > self.heap_list[smaller_child]:
                self.heap_list[index], self.heap_list[smaller_child] = (
                       self.heap_list[smaller_child], self.heap_list[index])
            index = smaller_child

    def _min_child(self, index):
        """Return the index of the smallest of a node's children."""
        index *= 2
        # If index now equals size(), the node only has one child.
        if index < self.size() and (
            self.heap_list[index] > self.heap_list[index + 1]):
                index += 1
        return index

    def pop(self):
        """Removes and returns the smallest item in the Heap.

        Raises an IndexError through peek() if the Heap is empty.
        """
        # Rely on peek() for heap size checking and getting the element.
        minimum = self.peek()
        # Position last item as new root
        self.heap_list[1] = self.heap_list[self.size()]
        # Remove last list item using list's pop, not this method.
        self.heap_list.pop()
        self._heap_down()
        return minimum
