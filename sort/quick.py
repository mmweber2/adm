def quicksort(sequence):
    """Returns a sorted copy of a list.

    Args:
        sequence: A list of data to sort. Items may be numbers, strings,
            or other comparable objects.

    Returns:
        A list copy of sequence in non-descending lexographic order.
    """
    if len(sequence) <= 1:
        return sequence
    mid = len(sequence) / 2
    pivot = _median_of_three(sequence)
    smaller_elements = []
    larger_elements = []
    for element in sequence[:mid] + sequence[mid + 1:]: # Add the pivot later
        if element <= pivot:
            smaller_elements.append(element)
        else:
            larger_elements.append(element)
    smaller_elements = quicksort(smaller_elements)
    larger_elements = quicksort(larger_elements)
    return smaller_elements + [pivot] + larger_elements

def _median_of_three(sequence):
    """Helper method for quicksort to pick median of 3 elements."""
    # Besides just returning the median of the first, middle, and last elements,
    # this function sorts them to help with future sub-sorts.
    # If sequence is only 2 elements, the "middle" and last element will be the
    # same, and since neither is less than the other, they will be left as is.
    # If sequence is only one element, all three elements will be the same,
    # but this should not happen, because quicksort returns before choosing
    # a pivot if the list is only a single element.
    mid = len(sequence) / 2
    # Sort first and last element
    if sequence[-1] < sequence[0]:
        sequence[-1], sequence[0] = sequence[0], sequence[-1]
    # Sort last element and middle element
    if sequence[-1] < sequence[mid]:
        sequence[-1], sequence[mid] = sequence[mid], sequence[-1]
    # Sort middle element and first element
    if sequence[mid] < sequence[0]:
        sequence[0], sequence[mid] = sequence[mid], sequence[0]
    return sequence[mid]
