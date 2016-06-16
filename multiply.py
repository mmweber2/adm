def multiply(a, b):
    """Multiplies integers a and b."""
    # We could special case a or b being 0 or 1, but those cases will
    # be resolved quickly anyway because they will be just a single digit
    result = 0
    # If both numbers are negative or positive, result will be positive, so we
    # only need to know if one is negative and other is not
    negative = True if ((a < 0 and b > 0) or (b < 0 and a > 0)) else False
    # TODO: Strip negative sign if it exists
    # Put shorter number first for consistency
    a, b = (str(a), str(b)) if a < b else (str(b), str(a))
    digit = 0
    while digit < len(a):
        multiplicant = int(a[digit]) * 10**digit
        for i in xrange(len(b)):
            result += multiplicant * (int(b[i]) * 10**i)
        digit += 1
    return result

