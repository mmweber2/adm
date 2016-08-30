def bin_pack(item_sizes, capacity):
    """Returns an estimate of the number of boxes needed to pack item_sizes.

    Uses the first-fit decreasing heuristic:
        Sort the items by size in decreasing order.
        For each item, place it in the first box that has room for it.
        If none of the boxes have room, create a new box.

    Args:
        item_sizes: list of item sizes (integers or floats) to pack.
            All sizes must be in the range 0 < size <= capacity.

        capacity: integer or float, the capacity of a single box.
            Must be a number >= the largest size in item_sizes.
            All boxes are assumed to have the same capacity.

    Raises:
        ValueError: at least one size in item_sizes is greater than capacity
            or is less than or equal to 0, or item_sizes contains
            a non-number item size.

        TypeError: capacity is not a number. 

    Returns:
        An integer estimate of the number of boxes required to pack every item
            in item_list into boxes of capacity size, including any partially
            filled boxes.
            Returns 0 if item_sizes is empty.
    """
    boxes = []
    sizes = sorted(item_sizes, reverse=True)
    for size in sizes:
        if size <= 0:
            raise ValueError("item size must be > 0")
        if size > capacity:
            # Also triggers if size is a string or None
            raise ValueError("invalid size: {}".format(size))
        placed_item = False
        for i in xrange(len(boxes)):
            if boxes[i] - size >= 0:
                # Item fits in an existing box
                boxes[i] -= size
                placed_item = True
                break
        if not placed_item:
            # Make a new box
            boxes.append(capacity - size)
    return len(boxes)



