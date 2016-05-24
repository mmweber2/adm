def longest_increasing_sequence(seq):
    """
    Finds the longest monotonically increasing subsequence of sequence seq.

    If there are multiple such subsequences of the maximum length, an
    arbitrary one is returned.

    Args:
        seq: A sequence of numbers.

    Returns:
        A list containing the longest monotonically increasing subsequence
        of numbers in seq.
    """
    # Index to max sequence length
    # In the worst case, each number is a sequence of 1
    lengths = [1 for _ in xrange(len(seq))]
    # For each index, store the index of its predecessor
    predecessors  = [None for _ in xrange(len(seq))]
    # First item has length 1 and no predecessor
    for i in xrange(1, len(seq)):
        for prev in xrange(0, i):
            # No improvement
            if lengths[prev] + 1 <= lengths[i]: continue
            if seq[i] > seq[prev]:
                lengths[i] = lengths[prev] + 1
                predecessors[i] = prev
    # Table is built, now find the longest sequence
    # We have the lengths, so we can look for the max
    max_length = max(lengths)
    longest_seq = []
    # No need to look at the first value, any index can be a sequence of 1
    for i in xrange(len(seq) - 1, 0, -1):
        if lengths[i] == max_length:
            longest_seq = [seq[i]]
            current = i
            while predecessors[current] != None:
                longest_seq.append(seq[current])
                current = predecessors[current]
            # If there are ties, just take the first one we see
            break
    # We added from largest to smallest, so reverse
    return longest_seq[::-1]





