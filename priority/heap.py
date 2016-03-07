# A data structure of ordered keys with quick access to smallest or largest
# key in the set.
class Heap(object):

    def __init__(self):
        self.size = 0
        # Start with 0 as index 0 for easy integer division.
        self.heap_list = [0]

    # Insert object with value value.
    def insert(self, value):
        self.heap_list.append(value)
        self.size += 1
        self._heapify(self.size)

    def _heapify(self, index):
        while index / 2 > 0:
            if self.heap_list[index] < self.heap_list[index / 2]:
                (self.heap_list[index], self.heap_list[index / 2]) = (
                    self.heap_list[index / 2], self.heap_list[index])
            index /= 2

