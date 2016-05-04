def subsets(array):
    """
    Generates all of the subsets of array.

    If the elements in array are not unique, duplicate elements will
    be included the same number of times that they appear in array.

    Args:
        array: The iterable of items from which to create subsets.

        remaining; The remaining items from which to create subsets.

    Raises:
        TypeError: array is not an iterable.
    """
    sets = []
    # Create subsets of one element
    #print "Calling with array ", array
    if len(array) == 0:
        return sets
    if len(array) == 1:
        sets.extend([[], [array[0]]])
        return sets
    else:
        smaller_sets = subsets(array[1:])
        sets.extend(smaller_sets)
        for subset in smaller_sets:
            sets.append([array[0]] + subset)
        return sets

