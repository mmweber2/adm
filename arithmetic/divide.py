from integer import BigInteger

def divide(a, b):
    """Returns the quotient of a divided by b.

    Args:
        a: The BigInteger to be divided; the dividend.
        b: The BigInteger to divide by; the divisor. May not be 0.

    Returns:
        A new BigInteger representing the quotient of a and b (a divided by b).

    Raises:
        ValueError: b is equal to 0.
    """
