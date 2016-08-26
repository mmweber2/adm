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
