from integer import BigInteger
from multiply import multiply

def divide(dividend, divisor):
    """Returns the integer divided quotient of a divided by b.

    Args:
        dividend: The BigInteger to be divided.
        divisor: The BigInteger to divide by; the divisor. May not be 0.

    Returns:
        A new BigInteger representing the quotient of dividend and divisor.
        Since this function performs integer division, any remainder will be
        stripped (i.e., 3 divided by 2 equals 1).

    Raises:
        ZeroDivisionError: divisor is equal to 0.
    """
    if divisor == BigInteger("0"):
        raise ZeroDivisionError("Cannot divide by zero")
    negative = dividend.negative ^ divisor.negative
    if dividend.negative:
        dividend = BigInteger._flip_sign(dividend)
    if divisor.negative:
        divisor = BigInteger._flip_sign(divisor)
    quotient = BigInteger("0")
    # Create table of divisor products for lookup
    product_table = []
    multiplicant = BigInteger("1")
    while True:
        product = multiply(multiplicant, divisor)
        product_table.append((multiplicant, product))
        if product > dividend:
            break
        multiplicant = multiply(multiplicant, BigInteger("2"))
    remainder = dividend
    # Start with biggest product less than dividend
    for i in xrange(len(product_table)-1, -1, -1):
        factor, product = product_table[i]
        if product <= remainder:
            quotient = BigInteger.add(quotient, factor)
            remainder = BigInteger.subtract(remainder, product)
        # Keep checking smaller products whether or not we found a match
    if negative:
        return BigInteger._flip_sign(quotient)
    return quotient
