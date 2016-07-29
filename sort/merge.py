def merge_sort(sequence):
    """Sorts a list using merge sort.

    Args:
        sequence: A list of data to sort. May consist of numbers, strings,
            or other comparable items.
    Returns:
        A list of the data in sequence in non-descending lexographic order.
    """
    if len(sequence) <= 1:
        # Per documentation, sequence should be a list already
        return sequence
    mid = len(sequence) / 2
    left = merge_sort(sequence[:mid])
    right = merge_sort(sequence[mid:])
    merged = []
    left_pos = 0
    right_pos = 0
    while True:
        if left[left_pos] <= right[right_pos]:
            merged.append(left[left_pos])
            left_pos += 1
            if left_pos == len(left):
                # Left is empty, add all remaining in right
                return merged + right[right_pos:]
        else:
            merged.append(right[right_pos])
            right_pos += 1
            if right_pos == len(right):
                # Right is empty, add all remaining in left
                return merged + left[left_pos:]
