from operator import itemgetter

class KDTree(object):
    """Represents a K-Dimensional tree.

    Creates a tree that partitions space by half-planes such that each object
    is contained in its own region.

    Once a tree has been created from training data, the data will be sorted
    among the k dimensions of the data. An approximation can then be found
    for the nearest neighbor of a new point in O(height) time.

    The data is split first among the first dimension, then the second
    dimension, and so on until it has been split by the kth dimension, then
    cycles back to the first dimension until each split contains a single
    point.
    """

    # TODO: Work in cells?

    def __init__(self, training_data):
        """Create a new KD tree.

        Args:
            training_data: List or tuple of k-length list or tuples, where
            k is an integer between 2 and 20 (inclusive).
            Each position represents a dimension, so the first item always
            represents the first dimension, the second a second dimension,
            and so on. Each list or tuple must contain the same number of
            dimensions.
            Items must all be of the same type (numbers, strings, etc), as the
            default comparator will be used to determine their ordering.
            Items must be immutable in order for comparisons to remain reliable.
        """
        data = training_data[:]
        dimension = 1
        median = _get_median(data, dimension)
        root = KDTreeNode(median[dimension], dimension)

    @staticmethod
    def _get_median(dataset, dimension):
        """Returns the median value of dataset according to dimension."""
        # Methods exist to find a median in shorter O(n) time than this, but
        # I'm using this simple method for now.
        dataset.sort(key=itemgetter(dimension-1))
        return dataset[len(dataset)/2]

    # TODO: Create function that sorts by a dimension, splits by that dimension,
    # then repeats on the next dimension

# TODO: Add child in correct place
class KDTreeNode(object):
    """Represents a single vertex in the KD Tree."""
    def __init__(self, value, dimension):
        """Create a new KD Tree vertex to use in a KDTree.

        Args:
            value: The value this Node represents. Can be a number, string,
            or other comparable type, but must be immutable and the same type
            as all other values in the KDTree.

            dimension: Integer representing the dimension among which this Node
            splits the data, or by which it has been split if it is a leaf Node.
            Dimensions are 1-indexed, so 1 and 2 are the acceptable dimensions
            for a 2-dimensional tree.
            Must be in the range 0 < dimension <= k.
        """
        self.value = value
        self.dimension = dimension
        self.left = None
        self.right = None
