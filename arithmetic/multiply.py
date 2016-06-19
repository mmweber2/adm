    def multiply(a, b):
    """Returns the product of integers a and b."""
    # We could special case a or b being 0 or 1, but those cases will
    # be resolved quickly anyway because they will be just a single digit
    result = 0
    # Put shorter number first for consistency
    a, b = (str(a), str(b)) if a < b else (str(b), str(a))
    negative = False
    if a[0] == "-":
        a = a[1:]
        negative = True
    if b[0] == "-":
        b = b[1:]
        # If both numbers are negative or positive, result will be positive
        negative = False if negative else True
    digit = 0
    while digit < len(a):
        multiplicant = int(a[-1 - digit]) * 10**digit
        for i in xrange(len(b)):
            result += multiplicant * (int(b[-1 -i]) * 10**i)
        digit += 1
    if negative:
        return -1 * result
    return result
