def partition(seq, k):
    """Second version of partition.

    Since this is a rewrite, documentation is minimal; see partition.py for
    full documentation.
    """
    min_maxes = [[None] * k for _ in xrange(len(seq))]
    dividers  = [[None] * k for _ in xrange(len(seq))]
    
    # Row[i] = seq contains values up to and including seq[i]
    # Col[i] = k = i + 1

    # Fill in all seq = seq[0] for all values of k
    for j in xrange(k):
        min_maxes[0][j] = seq[0]
    # Fill in min-maxes for seq[:j+1] when k = 1
    # Already filled out for seq[0], so start at 1
    for i in xrange(1, len(seq)):
        min_maxes[i][0] = min_maxes[i-1][0] + seq[i]

    # Fill in recurrences
    for j in xrange(1, k):
        for i in xrange(1, len(seq)):
            # Value must be <= value for k-1 since there are more partitions
            min_maxes[i][j] = min_maxes[i][j-1]
            # Keep track of the sum of the remaining numbers to avoid creating
            # a new sum each time
            remaining_sum = sum(seq[1:i+1])
            # Look at all partitions of seq up to j
            for x in xrange(i):
                # Get the largest number we'll have if we put a partition here
                local_max = max(min_maxes[x][j-1], remaining_sum)
                # If we move the partition one forward, the remaining sum will
                # be one element smaller
                remaining_sum -= seq[x + 1]
                if local_max <= min_maxes[i][j]:
                    min_maxes[i][j] = local_max
                    # x + 1 because that's where the sequence starts
                    dividers[i][j] = x + 1

    # Reconstruct partitions
    split = []
    start = dividers[-1][-1]
    end = len(seq)
    while True:
        # Starting at the end, so insert in reverse order
        split.insert(0, seq[start:end])
        k -= 1
        if k == 0:
            break
        end = start
        # One partition has been added, so get the one for k - 1 partitions
        start = dividers[start - 1][k - 1]
    print "Split was ", split
    print "Min max of this is ", min_maxes[-1][-1]
    return min_maxes[-1][-1]


