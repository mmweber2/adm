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

    Generates all combinations of subsets and chooses the smallest cover of the
    set union.
    If there are multiple such covers, returns one arbitrarily.

    Args:
        subsets: a list of sets. Each set may contain numbers, strings,
            or other hashable objects.

    Returns:
        A minimum-size list of sets from subsets that cover the union of all
            elements in subsets. Returns an empty list if subsets is empty.
    """
    if len(subsets) == 0:
        return []
    for i in xrange(1, 2**len(subsets)):
        # Start with covers of size 1 and increases size by 1 each time,
        # so the first cover found will be the smallest possible cover
        for cover in _generate_subsets(subsets, i):
            if _is_valid_cover(cover):
                return cover

def _is_valid_cover(all_subsets, cover):
    """Returns True iff cover is a valid set cover for all_subsets."""
    # Put all items of all_subsets or cover into sets
    covered = set(item for subset in cover for item in subset)
    union = set(item for subset in all_subsets for item in subset)
    return covered == union

def _generate_subsets(subsets, max_size=None):
    """Given a set of subsets, generate all combinations of subsets."""
    if max_size == 0:
        return []
    if max_size is None:
        max_size = len(subsets)
    if max_size < 0:
        raise ValueError("max_size cannot be negative")
    # Empty set is included in all subsets of size 1 or greater
    all_subsets = [[set()]]
    for i in xrange(2**len(subsets)):
        current = []
        for j in xrange(max_size):
            if j > i:
                break
            if i & (1 << j):
                current.append(subsets[j])
        if current:
            all_subsets.append(current)
    return all_subsets
