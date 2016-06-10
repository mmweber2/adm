from operator import itemgetter
from math import sqrt

class KDTree(object):
    """Represents a K-Dimensional tree.

    Creates a tree that partitions space by half-planes such that each object
    is contained in its own region.

    Once a tree has been created from data, the data will be sorted
    among the k dimensions of the data. The nearest neighbor of a new point
    can then be found in approximately O(height) time.

    The data is split first among the first dimension, then the second
    dimension, and so on until it has been split by the kth dimension, then
    cycles back to the first dimension until each split contains a single
    point.

    Dimensions are 1-indexed, such that a 2-D tree has dimensions (1, 2).
    """

    def __init__(self, data, dimension=1, error_checking=True):
        """Creates a new KD tree from a set of data.

        Each value in data contains all dimensions, so if k is 2 and value is
        (10, 5), the data point is (10, 5), and the tree will be sorted by
        one of those dimensions, as indicated by dimension below.

        Each position represents a dimension, so the first item always
        represents the first dimension, the second a second dimension,
        and so on. Each list or tuple must contain the same number of
        dimensions.

        All items in the iterables must be numbers, and the default comparator
        will be used to determine their ordering.
        In order for comparisons to remain reliable, items must not be changed
        after creating the tree.

        Args:
            data: List or tuple of k-length list or tuples of numbers, where
                k is an integer greater than 1.

            dimension: Integer representing the dimension among which this node
                splits the data, or by which it has been split if it is a leaf.
                Dimensions are 1-indexed, so 1 and 2 are the acceptable
                dimensions for a 2-dimensional tree.
                Must be in the range 0 < dimension <= k.

            error_checking: Boolean indicating whether data and dimension
                should be checked for errors. Defaults to True.

        Raises:
            IndexError: data contains data points of different lengths
                (dimensions).

            ValueError: dimension is outside the valid range.
        """
        # All points must have the same number of dimensions
        k = len(data[0])
        if error_checking:
            if k == 1:
                raise ValueError("Data values must have 2 or more dimensions")
            # Explicit check for uneven dimensions because the behavior may be
            # different depending on the position of the longer or shorter item
            for item in data[1:]:
                if len(item) != k:
                    raise IndexError("All items must contain k dimensions")
            if dimension <= 0 or dimension > k:
                raise ValueError("dimension must be in range 0 < dimension <= k")
        self.left = None
        self.right = None
        self.dimension = dimension
        # Don't recurse if node has no children
        if len(data) == 1:
            self.value = tuple(data[0])
            return
        median = KDTree._get_median_index(data, dimension)
        # _get_median_index sorts by dimension, so we can index to the median
        # Values should not be modified once they're added to the tree
        self.value = tuple(data[median])
        dimension = KDTree._get_next_dimension(k, dimension)
        # data is still sorted from the median check
        left_data = data[:median]
        right_data = data[median + 1:]
        if len(left_data) > 0:
            self.left = KDTree(left_data, dimension, False)
        if len(right_data) > 0:
            self.right = KDTree(right_data, dimension, False)

    @staticmethod
    def _get_next_dimension(k, dimension):
        """Get the next dimension by which to divide cells."""
        # Cycle back to the first dimension when we've divided by all of them
        return 1 if dimension == k else dimension + 1

    @staticmethod
    def _get_median_index(dataset, dimension):
        """Returns the index of the median value of dataset by dimension."""
        # Methods exist to find a median in O(n) time, but I'm using this
        # simple O(n log n) method for now.
        dataset.sort(key=itemgetter(dimension-1))
        return len(dataset)/2

    def print_tree(self):
        """Prints the KD Tree in level order.
        
        Each value will be in the following format:
         
        Value: (node value)
        Dimension: (dimension sorted by for that split)

        """
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            print "Value: ", current.value
            print "Dimension: ", current.dimension
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def find_closest(self, new_value):
        """Finds the closest value already in the Tree.

        Args:
            new_value: The list or tuple representing a data point for which to
                find a close value.
                Must be of length k (must have the same number of dimensions)
                and contain only numbers.

        Returns:
            A tuple representing the closest data point to new_value that is
                part of this KDTree.

        Raises:
            ValueError: new_value is not of length k.

            TypeError: new_value is not an iterable.
        """
        if len(new_value) != len(self.value):
            raise ValueError("new_value must be of length k")
        current = self
        closest_value = None
        min_distance = float("inf")
        # Order of areas to explore doesn't matter, but check all cells that
        # could have closer values
        explore_queue = []
        while True:
            distance = KDTree._get_distance(new_value, current.value)
            if distance < min_distance:
                closest_value = current.value
                min_distance = distance
            dimension = current.dimension
            # Go left
            if new_value[dimension-1] <= current.value[dimension-1]:
                explore_queue.append(current.left)
                # But, also consider right subtree
                for i in xrange(len(new_value)):
                    # Since all dimensions are checked here, an equal value in
                    # the current dimension will lead to checking both cells
                    if new_value[i] >= current.value[i]:
                        explore_queue.append(current.right)
            # Go right
            else:
                explore_queue.append(current.right)
                # But, also consider left subtree
                for i in xrange(len(new_value)):
                    if new_value[i] <= current.value[i]:
                        explore_queue.append(current.left)
            # None values will get added if we try to branch from a leaf
            explore_queue = [x for x in explore_queue if x is not None]
            if len(explore_queue) == 0:
                return closest_value
            current = explore_queue.pop()

    @staticmethod
    def _get_distance(p1, p2):
        """Returns the straight line distance between p1 and p2."""
        if len(p1) != len(p2):
            raise ValueError("_get_distance values must be of the same length")
        distance = 0
        for i in xrange(len(p1)):
            distance += (p1[i] - p2[i])**2
        return sqrt(distance)

# TODO: Find min in dth dimension
