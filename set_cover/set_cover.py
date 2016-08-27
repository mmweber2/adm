def set_cover(subsets):
    """Estimates the smallest set cover for the elements in subsets.

    Using a greedy heuristic, attempts to cover the union of all subsets
    through the smallest number of those subsets.

    Args:
        subsets: a list of sets. Each set may contain numbers, strings,
            or other hashable objects.

    Returns:
        A list of sets from subsets that cover the union of all elements
            in subsets.
    """
    cover = []
    union = set()
    covered = set()
    for subset in subsets:
        union.update(subset)
    remaining_subsets = sorted(subsets, key=lambda x: len(x - covered))
    while len(union) > 0:
        largest = remaining_subsets.pop()
        cover.append(largest)
        covered.update(largest)
        union -= largest
        remaining_subsets.sort(key=lambda x: len(x - covered))
    return cover

def set_cover_exact(subsets):
    """Returns the smallest set cover for the elements in subsets.

    Generates all combinations of subsets and chooses the smallest subset of
    subsets that covers the set union.
    If there are multiple such subsets, returns one arbitrarily.

    Args:
        subsets: a list of sets. Each set may contain numbers, strings,
            or other hashable objects.

    Returns:
        A minimum-size list of sets from subsets that cover the union of all
            elements in subsets.
    """
    # TODO: Write set cover; this just generates all subsets
    perms = _generate_subsets(subsets)
    for x in perms:
        print "Subset: ", x

def _generate_subsets(subsets):
    all_subsets = []
    for i in xrange(2**len(subsets)):
        current = []
        for j in xrange(len(subsets)):
            if j > i:
                break
            if i & (1 << j):
                current.append(subsets[j])
        all_subsets.append(current)
    return all_subsets

set_cover_exact([set((1, 2, 3)), set((4, 5)), set((2, 3))])
