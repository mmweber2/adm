def subsets(input_list):
    """
    Generates all of the subsets of input_list.

    If the elements in input_list are not unique, duplicate elements will
    be included the same number of times that they appear in input_list.

    Args:
        input_list: The list or tuple of items from which to create subsets.

    Returns:
        A list of lists, where each list is a subset of input_list.
        If input_list is an empty list, returns an empty list.

    Raises:
        TypeError: input_list is not a list.
    """
    # Just return empty list for empty input_list
    if len(input_list) == 0:
        return []
    if type(input_list) not in (list, tuple):
        raise TypeError("input_list must be a list or tuple")
    sets = []
    # Create subsets of one element
    if len(input_list) == 1:
        sets.extend([[], [input_list[0]]])
    else:
        smaller_sets = subsets(input_list[1:])
        sets.extend(smaller_sets)
        for subset in smaller_sets:
            sets.append([input_list[0]] + subset)
    return sets
