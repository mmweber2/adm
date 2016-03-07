# A data structure of ordered keys with quick access to smallest or largest
# key in the set.
class Heap(object):

    def __init__(self):
        self.size = 0
        # Start with 0 as index 0 for easy integer division.
        self.heap_list = [0]

    # Insert object with value value.
    def push(self, value):
        self.heap_list.append(value)
        self.size += 1
        self._heap_up(self.size)

    # For insertion; bring a newly added value up to its proper index,
    #    instead of at the end of the array.
    def _heap_up(self, index):
        while index / 2 > 0:
            if self.heap_list[index] < self.heap_list[index / 2]:
                (self.heap_list[index], self.heap_list[index / 2]) = (
                    self.heap_list[index / 2], self.heap_list[index])
            index /= 2

    # For deletion; bring a newly moved value down from the root to
    #    its proper index.
    def _heap_down(self):
        # Always start at the (newly changed) root.
        index = 1
        # Index has at least one child
        while index * 2 <= self.size:
            smaller_child = self._min_child(index)
            if self.heap_list[index] > self.heap_list[smaller_child]:
                self.heap_list[index], self.heap_list[smaller_child] = (
                       self.heap_list[smaller_child], self.heap_list[index])
            index = smaller_child

    # Return the index of the smallest of a node's children.
    def _min_child(self, index):
        index *= 2
        print "Looking at index ", index
        if index < self.size and ( 
            self.heap_list[index] > self.heap_list[index + 1]):
                index += 1
        return index

    # Raises an IndexError if list is empty.
    def pop(self):
        if self.size == 0:
          raise IndexError("No items to pop.")
        minimum = self.heap_list[1]
        # Position last item as new root
        self.heap_list[1] = self.heap_list[self.size]
        # Remove old last item
        self.heap_list.pop()
        self.size -= 1
        self._heap_down()
        return minimum


#TODO: More comments!
