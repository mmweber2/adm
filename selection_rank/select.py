import random
def get_rank(array, k):
    """Returns the kth smallest item in array.

    Args:
        array: list of comparable items to search. Does not need to be in sorted
            order, and duplicate elements are permitted.

        k: integer, the ranking of the item to return.
            For example, if you were looking for the median of an odd number
            of items, k would be len(array) / 2.
            Must be in the range 0 <= k < len(array).

    Returns:
        The item in array that belongs at the kth index if array were fully
            sorted, or None if array is empty.

    Raises:
        IndexError: k is not a valid index for array.
    """
    if len(array) == 0:
        return None
    if k < 0 or k >= len(array):
        raise IndexError("k must be a valid index for array")
    pivot = random.choice(array)
    # Elements in array <= pivot
    smaller = []
    greater = []
    for element in array:
        if element < pivot:
            smaller.append(element)
        else:
            greater.append(element)
    if k == len(smaller):
        # pivot was the kth item
        # This will always be the case if len(array) = 1
        return pivot
    if k == len(smaller) - 1:
        # k is largest element in smaller
        return get_rank(smaller, len(smaller) - 1)
    if k < len(smaller):
        # k is somewhere in smaller
        return get_rank(smaller, k)
    else:
        # k is somewhere in greater, adjust k to note the smaller elements
        return get_rank(greater, k - len(smaller))
