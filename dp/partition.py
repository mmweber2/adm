def partition(seq, k):
    """Partitions seq into k equal ranges without reordering seq.

    Each partition seeks to minimize the maximum sum of all the ranges.
    For example, if seq is [1, 2, 3, 4, 5, 6, 7, 8, 9], the best partition
    for k = 3 would be [(1, 2, 3, 4, 5), (6, 7), (8, 9)]. This would give
    sums of 15, 13, and 17.

    Args:
        seq: Sequence of numbers to partition. Must contain at least one
        item.

        k: Integer, the number of partitions to create. Must be greater
        than 0.

    Returns:
        A k-length list of indices after which to place the partitions.

    Raises:
        IndexError: seq is empty, or k <= 0.
    """
    # Figure out chart for k = 1
    # For each index and each k, get the min maximum we can do
    # from that division, assuming we are starting from index i
    # DP table for values, DP table for dividers, prefix sums array

    # First number will have no previous numbers to add to it
    prefix_sums = [0]
    # For each index, the sum of that number plus all the previous numbers
    for i in xrange(len(seq)):
        prefix_sums.append(prefix_sums[-1] + seq[i])
    print "Prefix: %r" % prefix_sums

    # The min_max for each index and value of k 
    min_maxes = [[None] * k for _ in xrange(len(seq))]
    print "Min Maxes: %r" % min_maxes
    # Divider positions (index of first item in partition) for each partition
    dividers = [[None] * k for _ in xrange(len(seq))]

    # Fill in column where k = 1, so min_maxes are all items in that subarray
    for i in xrange(len(seq)):
        min_maxes[i][0] = prefix_sums[i+1]
    print "Min Maxes: %r" % min_maxes
    # Fill in row 1 for each value of k when there is only one value in seq
    for j in xrange(k):
        min_maxes[0][j] = seq[0]
    print "Min Maxes: %r" % min_maxes

    for i in xrange(1, len(seq)):
        for j in xrange(1, k):
            min_maxes[i][j] = float("inf")
            for x in xrange(i):
                cost = max(min_maxes[x][j-1], prefix_sums[i+1] - prefix_sums[x+1])
                if cost < min_maxes[i][j]:
                    min_maxes[i][j] = cost
                    dividers[i][j] = x

    # TODO: Reconstruct partition
    print "Seq:"
    print seq
    print "Result:"
    print min_maxes
    return min_maxes[-1][-1]
