def subsets(array):
    """
    Generates all of the subsets of array.

    If the elements in array are not unique, duplicate elements will
    be included the same number of times that they appear in array.

    Args:
        array: The iterable of items from which to create subsets.

    Returns:
        A list of lists, where each list is a subset of array.
        If array is an empty iterable, returns an empty list.

    Raises:
        TypeError: array is not an iterable.
    """
    # Just return empty list for empty array
    if len(array) == 0:
        return []
    sets = []
    # Create subsets of one element
    if len(array) == 1:
        sets.extend([[], [array[0]]])
    else:
        smaller_sets = subsets(array[1:])
        sets.extend(smaller_sets)
        for subset in smaller_sets:
            sets.append([array[0]] + subset)
    return sets

