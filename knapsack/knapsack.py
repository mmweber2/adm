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

    Args:
        itemset: List of tuples in the form (size, value) where size is an
            integer and value is a float.

        capacity: Integer indicating the maximum sum of sizes that fit within
            this knapsack.

    Returns:
        A list of items with a sum of sizes less than equal to capacity and
        the maximum sum of values.
    """
    # TODO: Is it the maximum sum? A good sum?
    # Trying the method on line 8
    max_values = [(0, capacity)]
    # TODO: Add another dictionary for backtracking
    for i in xrange(len(itemset)):
        size, value = itemset[i]
        # This item doesn't fit, so it doesn't improve the solution
        if size > capacity:
            max_values.append(max_values[-1])
        else:
            previous_best = max_values[(i-1, capacity)]
            # Value if we include this item
            with_i = max_values[(i-1, capacity-size)] + value
            max_values.append(max(previous_best, with_i))
    return max_values[(n, capacity)]

        


