from time import sleep

def quicksort(sequence, start=0, end=None):
    """Returns a sorted copy of a list.

    Args:
        sequence: A list of data to sort. Items may be numbers, strings,
            or other comparable objects.
        start: integer, the index of the array to begin sorting.
            Defaults to 0.
        end: integer, the index of the array at which to end
            sorting (inclusive). Defaults to None.

    Returns:
        A list copy of sequence in non-descending lexographic order.
    """
    if end is None:
        end = len(sequence) - 1
    # Nothing to sort
    if start >= end:
        return sequence
    pivot = _median_of_three(sequence, start, end)
    left = start
    right = end
    while left <= right:
        while sequence[left] < pivot:
            left += 1
        while sequence[right] > pivot:
            right -= 1
        if left <= right:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            # These two elements are sorted, so try the next ones
            left += 1
            right -= 1
    # To get here, right < left, so this is the first half of sequence
    quicksort(sequence, start, right)
    # left > right, so this is the second half of sequence
    quicksort(sequence, left, end)
    return sequence

def _median_of_three(sequence, start=0, end=None):
    """Helper method for quicksort to pick median of 3 elements."""
    # Besides just returning the median of the first, middle, and last elements,
    # this function sorts them to help with future sub-sorts.
    if end is None:
        end = len(sequence) - 1
    # If sequence is only 2 elements, the "middle" and last element will be the
    # same, and since neither is less than the other, they will be left as is.
    # If sequence is only one element, all three elements will be the same,
    # but this should not happen, because quicksort returns before choosing
    # a pivot if the list is only a single element.
    mid = (start + end + 1) / 2
    # Sort first and last element
    if sequence[end] < sequence[start]:
        sequence[end], sequence[start] = sequence[start], sequence[end]
    # Sort last element and middle element
    if sequence[end] < sequence[mid]:
        sequence[end], sequence[mid] = sequence[mid], sequence[end]
    # Sort middle element and first element
    if sequence[mid] < sequence[start]:
        sequence[start], sequence[mid] = sequence[mid], sequence[start]
    return sequence[mid]
