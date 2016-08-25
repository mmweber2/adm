def bin_pack(item_list, capacity):
    """Returns an estimate of the number of boxes needed to pack item_list.

    Uses the first-fit decreasing heuristic:

    Sort the boxes by size in decreasing order.
    For each item, place it in the first box that has room for it.
    If none of the boxes have room, create a new box.

    Args:
        item_list: list of item sizes (numbers), where all items must be packed.
            All items must have sizes > 0.

        capacity: number, the capacity of a single box. Must be > 0.
            All boxes are assumed to have the same capacity.

    Returns:
        An integer estimate of the number of boxes required to pack every item
            in item_list into boxes of capacity size, including any partially
            filled boxes.

    Raises:
        ValueError: capacity is <= 0, or at least one size in item_list is <= 0.
    """

