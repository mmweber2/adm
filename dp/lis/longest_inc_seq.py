def longest_increasing_sequence(seq):
    """
    Finds the longest monotonically increasing subsequence of numbers in seq.

    If there are multiple such subsequences of the maximum length, an
    arbitrary one is returned.

    For example, if seq is [2, 4, 3, 5, 1, 7, 6, 9, 8], the longest
    monotonically increasing subsequence is of length 5, and one such
    sequence is [2, 4, 5, 7, 9].
    If seq is an empty sequence or only contains one element, returns seq.

    Items will be compared by the default comparator, so the sequence may not
    be monotonically increasing if seq contains items that are not numbers.

    Args:
        seq: A sequence of numbers.

    Returns:
        A list containing the longest monotonically increasing subsequence
        of numbers in seq.
    """
    # An empty sequence will bypass the table creation, but will cause
    # a ValueError from max() later on.
    if seq == []:
        return seq
    # Array of max sequence lengths corresponding to seq
    # In the worst case, each number is a sequence of 1
    lengths = [1 for _ in xrange(len(seq))]
    # For each index, store the index of its predecessor
    predecessors = [None for _ in xrange(len(seq))]
    # First item has length 1 and no predecessor
    for i in xrange(1, len(seq)):
        for prev in xrange(0, i):
            # No improvement
            if lengths[prev] + 1 <= lengths[i]: continue
            if seq[i] > seq[prev]:
                lengths[i] = lengths[prev] + 1
                predecessors[i] = prev
    # Table is built, now find the longest sequence
    longest_seq = []
    # Start from the far end because it is more likely to have longer sequences
    for i in xrange(len(seq) - 1, -1, -1):
        if lengths[i] > len(longest_seq):
            longest_seq = []
            current = i
            while current != None:
                longest_seq.append(seq[current])
                current = predecessors[current]
    # We added from largest to smallest, so reverse
    return longest_seq[::-1]





