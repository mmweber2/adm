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
        items: List of tuples in the form (size, value) where size is an
            integer and value is a float. Size must be a positive integer
            and value must be a float.

        capacity: Integer indicating the maximum sum of sizes that fit within
            this knapsack. Must be non-negative.

    Returns:
        A list of items with a sum of sizes less than equal to capacity and
            the maximum sum of values. Returns an empty list if items is empty
            or if capacity is 0.

    Raises:
        IndexError: capacity is < 0, or at least one item has a negative size.
    """

    # TODO: Is it the maximum sum? A good sum?
    # Trying the method on line 9

    if len(items) == 0 or capacity == 0:
        return []
    
    # 1-index columns to allow for an "empty" first item; if the first
    # item is too big, we need to have a zero-value item to put in
    # the table.
    # 1-index rows so that the row [capacity] is actually the best
    # known value for capacity.
    max_values = [([0] * (len(items) + 1)) for _ in xrange(capacity + 1)]
    for i in xrange(1, len(items) + 1):
        size, value = items[i-1]
        # Loop over partial capacities
        for j in xrange(capacity + 1):
            # This item doesn't fit, so it doesn't improve the solution
            if size > j:
                max_values[j][i] = max_values[j][i-1]
            else:
                previous_best = max_values[j][i-1]
                # Value if we include this item
                with_i = max_values[j-size][i-1] + value
                max_values[j][i] = max(with_i, previous_best)
    return reconstruct_subset(max_values, items)

def reconstruct_subset(max_values, items):
    subset = []
    # Avoid passing capacity as a parameter
    capacity = len(max_values) - 1
    for i in xrange(len(items)-1, -1, -1):
        size, value = items[i]
        # This item was included, so look at table result for ith item
        if max_values[capacity][i+1] == max_values[capacity-size][i] + value:
            subset.append(i)
            # Reduce available capacity
            capacity -= size
    return [items[index] for index in subset]
