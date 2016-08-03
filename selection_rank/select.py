from time import sleep

def get_rank(array, k, start=0, end=None):
    """Returns the kth smallest item in array.

    Args:
        array: list of comparable items to search. Does not need to be in sorted
            order, and duplicate elements are permitted.
            This function modifies the list.

        k: integer, the ranking of the item to return.
            For example, if you were looking for the median of an odd number
            of items, k would be len(array) / 2.
            Must be in the range 0 <= k < len(array).

        start: integer, the index at which to begin ranking. Defaults to 0.

        end: integer, the index at which to end ranking (inclusive).
            Defaults to the last item in array.

    Returns:
        The item in array that belongs at the kth index if array were fully
            sorted, or None if array is empty.

    Raises:
        IndexError: k is not a valid index for array.
    """
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError("k must be a valid index for this array")
    # Only one item in this partition
    if start == end and k == 0:
        return array[start]
    # Absolute pivot position (across all of array)
    abs_pivot = partition(array, start, end)
    # Relative pivot position; size of this left partition
    left_size = abs_pivot - start
    if k == left_size:
        # Found the exact index of k
        return array[abs_pivot]
    if k < left_size:
        # Recurse on left side of partition, exclude pivot itself
        return get_rank(array, k, start, abs_pivot - 1)
    else:
        # Recurse on right side of partition, exclude pivot itself
        # Adjust k to account for elements on left (including pivot)
        return get_rank(array, k - left_size - 1, abs_pivot + 1, end)

def partition(array, start, end):
    """Helper function for get_rank."""
    pivot = array[end]
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[swap_pos], array[i] = array[i], array[swap_pos]
            swap_pos += 1
    array[swap_pos], array[end] = array[end], array[swap_pos]
    return swap_pos

