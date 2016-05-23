def edit_distance(s1, s2):
    """Returns the Levenshtein distance between s1 and s2.

    For example, returns 0 if the strings are identical,
    1 if there is one different character, or the length
    of the other string if one of the strings is empty.

    Args:
        s1, s2: Strings between which to find the edit distance.

    Returns:
        An integer indicating the edit distance between s1 and s2.
    """
    if s1 == s2:
        return 0
    # TODO: Other cases
