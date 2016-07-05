from integer import BigInteger
from divide import divide
from multiply import multiply

def power(base, exponent):
    """Returns base to the power of exponent.

    Neither BigInteger is modified during this operation.

    Args:
        base: BigInteger, the number to be multiplied.

        exponent: BigInteger, the exponent to apply to the base.

    Returns:
        A new BigInteger of the result of base**exponent.
    """
    # TODO: Negative exponents
    if exponent == BigInteger("0"):
        return BigInteger("1")
    if exponent == BigInteger("1"):
        return base
    # Using 2 multiple times, so avoid creating new objects repeatedly
    two_int = BigInteger("2")
    half_exponent = divide(exponent, two_int)
    half_result = power(base, half_exponent)
    # a**n = a**(n/2) * 2 if n is even
    result = multiply(half_result, half_result)
    # Divide doesn't support mod or remainder, so check for an even number
    if multiply(half_exponent, two_int) == exponent:
        return result
    # Exponent is odd, so multiply by base one more time
    return multiply(result, base)
