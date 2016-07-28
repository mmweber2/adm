def quicksort(sequence):
    """Returns a sorted list of the data in sequence.

    Args:
        sequence: An iterable of data to sort. May be a list, tuple, string,
            or other sequence of comparable objects.

    Returns:
        A list of the data in sequence in non-descending lexographic order.
    """
    if len(sequence) <= 1:
        return list(sequence)
    mid = len(sequence) / 2
    # TODO:
    # Pick three pivots and take the median
    # Choosing the first, last, and middle element should help us avoid
    # a bad pivot, especially if sequence is already sorted
    pivot = sequence[mid]
    smaller_elements = []
    larger_elements = []
    # Don't sort the pivot
    for element in sequence[:mid] + sequence[mid + 1:]:
        if element <= pivot:
            smaller_elements.append(element)
        else:
            larger_elements.append(element)
    smaller_elements = quicksort(smaller_elements)
    larger_elements = quicksort(larger_elements)
    return smaller_elements + [pivot] + larger_elements




