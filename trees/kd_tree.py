from operator import itemgetter

class KDTree(object):
    """Represents a K-Dimensional tree.

    Creates a tree that partitions space by half-planes such that each object
    is contained in its own region.

    Once a tree has been created from data, the data will be sorted
    among the k dimensions of the data. An approximation can then be found
    for the nearest neighbor of a new point in O(height) time.

    The data is split first among the first dimension, then the second
    dimension, and so on until it has been split by the kth dimension, then
    cycles back to the first dimension until each split contains a single
    point.

    Dimensions are 1-indexed, such that a 2-D tree has dimensions (1, 2).

    Each node in the KDTree has the following attributes:
        value: The value iterable by which this node splits the data.

        k: An integer representing the total number of dimensions this tree
        considers. Equal to len(value) for any value in the tree.

        dimension: An integer representing the dimension that that particular
        node will split by. The root always splits by dimension 1.

        left, right: Pointers to this node's left and right children,
        which may be None.
    """

    def __init__(self, value, dimension):
        """Create a new KD Tree subtree.

        Each value contains all dimensions, so if k is 2 and value is
        (10, 5), the data point is (10, 5), and the tree will be sorted by
        one of those dimensions, as indicated by dimension below.
        The tree's k is equal to len(value).

        Args:
            value: The iterable of numbers this node represents.

            dimension: Integer representing the dimension among which this Node
            splits the data, or by which it has been split if it is a leaf Node.
            Dimensions are 1-indexed, so 1 and 2 are the acceptable dimensions
            for a 2-dimensional tree.
            Must be in the range 0 < dimension <= k.

        Raises:
            ValueError: dimension is outside the valid range.

            TypeError: value is not an iterable.
        """
        # Values should not be modified once they're added to the tree
        self.value = tuple(value)
        if dimension <= 0 or dimension > len(value):
            raise ValueError("dimension must be in range 0 < dimension <= k")
        self.dimension = dimension
        self.left = None
        self.right = None
    
    # TODO: Incorporate this into __init__.
    @staticmethod
    def build_tree(data):
        """Create a new KD tree from a set of data.

        Each position represents a dimension, so the first item always
        represents the first dimension, the second a second dimension,
        and so on. Each list or tuple must contain the same number of
        dimensions.
        Items must all be of the same type (numbers, strings, etc), as the
        default comparator will be used to determine their ordering.
        Items must not be changed after creating the tree in order for
        comparisons to remain reliable.

        Args:
            data: List or tuple of k-length list or tuples, where
            k is an integer greater than 1.

        Returns:
            A KDTree object as described in the class documentation.

        Raises:
            ValueError: data points contain an invalid number of
            dimensions.

            IndexError: data contains data points of different lengths
            (dimensions).
        """
        k = len(data[0])
        if k == 1:
            raise ValueError("Data values must have 2 or more dimensions")
        # Explicit check for uneven dimensions because the behavior may be
        # different depending on the position of the longer or shorter item
        for item in data[1:]:
            if len(item) != k:
                raise IndexError("All items must contain k dimensions")
        return KDTree._build_tree_inner(data[:], 1)

    # TODO: Incorporate this into __init__
    @staticmethod
    def _build_tree_inner(data, dimension):
        """Create a new subtree for a KD tree."""
        if data == []:
            return None
        median = KDTree._get_median_index(data, dimension)
        # _get_median_index sorts by dimension, so we can index to the median
        root = KDTree(data[median], dimension)
        # All points must have the same number of dimensions
        k = len(data[0])
        dimension = KDTree._get_next_dimension(k, dimension)
        # _get_median sorts by this dimension, so we can divide data
        root.left = KDTree._build_tree_inner(data[:median], dimension)
        root.right = KDTree._build_tree_inner(data[median + 1:], dimension)
        return root

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

    # TODO: Rework to use calculated distance, not just find the cell
    def find_closest(self, new_value):
        """Finds an approximation of the closest value already in the Tree.

        Returns the value in the same cell in which new_value would be found,
        if it were part of the tree. This value may not be the closest value
        across all dimensions, and is an approximation.

        Args:
            new_value: The data point for which to find a close value.
            Must be of length k (must have the same number of dimensions) and
            contain the same data type (numbers, strings, etc) as items already
            in the tree.

        Returns:
            An approximation of the closest data point in the KD Tree.
        """
        dimension = 1
        subtree = self
        closest_value = subtree.value
        while True:
            # No further divisions, so this must be the closest existing value
            if subtree == None:
                return closest_value
            closest_value = subtree.value
            if new_value[dimension-1] <= subtree.value[dimension-1]:
                subtree = subtree.left
            else:
                subtree = subtree.right
            # Hold onto last value we've seen
            dimension = KDTree._get_next_dimension(len(new_value), dimension)

# TODO: Find min in dth dimension
