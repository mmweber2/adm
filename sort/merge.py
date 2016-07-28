def merge_sort(sequence):
    """Sorts sequence using merge sort.

    Args:
        sequence: An iterable of data to sort. May be numbers, strings, or other
            comparable items.
    Returns:
        A list of the data in sequence in non-descending lexographic order.
    """
    if len(sequence) <= 1:
        # Convert to list, but don't nest if it's already a list
        return list(sequence)
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
