def edit_distance(s1, s2):
    """Returns the Levenshtein distance between s1 and s2.

    For example, returns 0 if the strings are identical, 1 if there is one
    different character, or the length of the other string if one of the
    strings is empty.

    Args:
        s1, s2: Strings between which to find the edit distance.

    Returns:
        An integer indicating the edit distance between s1 and s2.
    """
    if s1 == s2:
        return 0
    len1, len2 = len(s1), len(s2)
    if len1 == 0 or len2 == 0:
        return max(len1, len2)
    # Use 1-indexing so we can compare each to an empty string
    distance = [[None] * (len1 + 1) for _ in xrange(len2 + 1)]
    # Initialize first row and column
    for j in xrange(len1 + 1):
        distance[0][j] = j
    for i in xrange(len2 + 1):
        distance[i][0] = i
    # Find the edit distances
    for i in xrange(1, len2 + 1):
        for j in xrange(1, len1 + 1):
            swap_cost = distance[i-1][j-1] + (0 if s1[j-1] == s2[i-1] else 1)
            del_cost = distance[i-1][j] + 1
            insert_cost = distance[i][j-1] + 1
            distance[i][j] = min(swap_cost, del_cost, insert_cost)
    return distance[len2][len1]
