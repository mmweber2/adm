from collections import defaultdict
from collections import namedtuple
# A set of items S where item i has size si and value vi. Knapsack has capacity C.
# Find the subset that maximizes the value of values, given that total size is less
# than C.

# Check if all cost/value or size is the same
# If value per size is the same, it becomes an integer partition problem
# If the sizes and C are all integers and C <= 1000, you can use dynamic programming

def knapsack(items, capacity):
    """Finds the highest-value subset of item that fit within capacity.

    Each item has both a size and a value, and this function returns the
    set with the maximum sum of values that has a size <= capacity.

    If there are multiple possible subsets with the same value, one will
    be returned arbitrarily.

    Args:
        itemset: List of tuples in the form (size, value) where size is an
            integer and value is a float.

        capacity: Integer indicating the maximum sum of sizes that fit within
            this knapsack.

    Returns:
        A list of items with a sum of sizes less than equal to capacity and
            the maximum sum of values. Returns an empty list if items is empty
            or if capacity is 0.
    """

    # TODO: Is it the maximum sum? A good sum?
    # Trying the method on line 9

    if len(items) == 0 or capacity == 0:
        return []
    
    # 1-index columns to allow for an "empty" first item; if the first
    # item is > capacity, we need to have a zero-value item to put in
    # the table.
    # 1-index rows so that the row [capacity] is actually the best
    # known value for capacity.
    max_values = [([0] * (len(items) + 1)) for _ in xrange(capacity + 1)]
    # List of indices of items that make up the best subset out of each
    # partial item selection for each capacity
    best_subsets = [([] * (len(items) + 1)) for _ in xrange(capacity + 1)]
    for i in xrange(1, len(items)):
        size, value = items[i]
        # # This item doesn't fit, so it doesn't improve the solution
        if size > capacity:
            max_values[i][capacity] = max_values[i-1][capacity]
            best_subsets[i][capacity] = best_subsets[i-1][capacity]
        else:
            previous_best = max_values[i-1][capacity]
            # Value if we include this item
            with_i = max_values[i-1][capacity-size] + value
            if with_i > previous_best:
                max_values[i][capacity] = with_i
                best_subsets[i][capacity] = best_subsets[i-1][capacity-size] + [i]
    print "Best subsets:"
    print best_subsets[-1]
    return best_subsets[-1][capacity]

        


