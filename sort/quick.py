def quicksort(sequence, start=0, end=None):
    """Sorts sequence using QuickSort.

    Args:
        sequence: A list of data to sort. Items may be numbers, strings,
            or other comparable objects.
        start: integer, the index of the list to begin sorting.
            Defaults to 0.
        end: integer, the index of the list at which to end sorting (inclusive).
            Defaults to the last element in sequence.
    """
    if end is None:
        end = len(sequence) - 1
    # Nothing to sort
    if start >= end:
        return
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

def quicksort2(sequence, start=0, end=None):
    """Alternate version of quicksort."""
    if end is None:
        end = len(sequence) - 1
    if start < end:
        pivot_pos = partition(sequence, start, end)
        quicksort2(sequence, start, pivot_pos - 1)
        quicksort2(sequence, pivot_pos + 1, end)

def partition(sequence, start, end):
    """Helper function for quicksort2."""
    pivot = sequence[end]
    swap_pos = start
    # Don't check pivot position at end, swap it in later
    for i in xrange(start, end):
        if sequence[i] <= pivot:
            sequence[i], sequence[swap_pos] = sequence[swap_pos], sequence[i]
            swap_pos += 1
    # Everything else is partitioned, so put the pivot in its correct spot
    sequence[swap_pos], sequence[end] = sequence[end], sequence[swap_pos]
    return swap_pos

def _median_of_three(sequence, start=0, end=None):
    """Helper function for quicksort to pick median of 3 elements."""
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
