def partition(seq, k):
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
            # Look at all partitions of seq up to j
            for x in xrange(i):
                # Get the largest number we'll have if we put a partition here
                local_max = max(min_maxes[x][j-1], sum(seq[x + 1:i + 1]))
                if local_max <= min_maxes[i][j]:
                    min_maxes[i][j] = local_max
                    dividers[i][j] = x

    print "At the end, min_maxes is:"
    print min_maxes
    # TODO: Reconstruct sequences
    return min_maxes[-1][-1]


