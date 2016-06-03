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

    Dimensions are 1-indexed, such that a 2-D tree has dimensions (1, 2).

    Each node in the KDTree has the following attributes:
        value: The value by which this node splits the data.

        k: An integer representing the total number of dimensions this tree
        considers.

        dimension: An integer representing the dimension that that particular
        node will split by. The root always splits by dimension 1.

        left, right: Pointers to this node's left and right children,
        which may be None.
    """

    def __init__(self, value, k, dimension):
        """Create a new KD Tree subtree.

        Args:
            value: The value this Node represents. Can be a number, string,
            or other comparable type, but must be immutable and the same type
            as all other values in the KDTree.

            k: Integer representing the total number of dimensions contained in
            this tree. Must be > 0.

            dimension: Integer representing the dimension among which this Node
            splits the data, or by which it has been split if it is a leaf Node.
            Dimensions are 1-indexed, so 1 and 2 are the acceptable dimensions
            for a 2-dimensional tree.
            Must be in the range 0 < dimension <= k.
        """
        self.value = value
        self.k = k
        self.dimension = dimension
        self.left = None
        self.right = None
    
    @staticmethod
    def build_tree(training_data):
        """Create a new KD tree from a set of data.

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
        self.left = None
        self.right = None
        return KDTree._build_tree_inner(training_data[:], 1)

    @staticmethod
    def _build_tree_inner(data, dimension):
        """Create a new subtree for a KD tree."""
        if data == None:
            return None
        mid = len(data) / 2
        median = KDTree._get_median_index(data, dimension)
        # All points must have the same number of dimensions
        k = len(data)[0]
        root = KDTree(data[median], k, dimension)
        dimension = root._get_next_dimension(dimension)
        # _get_median sorts by this dimension, so we can divide data
        root.left = _build_tree(data[:median], dimension)
        root.right = _build_tree(data[median + 1:], dimension)
        return root

    def _get_next_dimension(self, dimension):
        """Get the next dimension by which to divide cells."""
        # Cycle back to the first dimension when we've divided by all of them
        if dimension == self.k:
            return 1
        return dimension + 1

    @staticmethod
    def _get_median_index(dataset, dimension):
        """Returns the index of the median value of dataset by dimension."""
        # Methods exist to find a median in shorter O(n) time than this, but
        # I'm using this simple method for now.
        dataset.sort(key=itemgetter(dimension-1))
        return len(dataset)/2

