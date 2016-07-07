from integer import BigInteger
from divide import divide
from multiply import multiply

def power(base, exponent, cache=None):
    """Returns base to the power of exponent.

    If exponent is less than 0, returns a BigInteger of 0.

    Neither BigInteger is modified during this operation.

    Args:
        base: BigInteger, the number to be multiplied.

        exponent: BigInteger, the exponent to apply to the base.

    Returns:
        A new BigInteger of the result of base**exponent.
    """
    if cache is None:
        cache = {}
    # Any negative exponent will be a fraction 0 < x < 1, so round down to 0
    if exponent < BigInteger("0"):
        return BigInteger("0")
    if exponent == BigInteger("0"):
        return BigInteger("1")
    if exponent == BigInteger("1"):
        return base
    if exponent in cache:
        return cache[exponent]
    half_exponent = divide(exponent, BigInteger("2"))
    half_result = power(base, half_exponent)
    # a**n = a**(n/2) * 2 if n is even
    result = multiply(half_result, half_result)
    # Divide doesn't support mod or remainder, so check for an odd number
    # If exponent is odd, multiply by base one more time
    if exponent.digits[-1] in (1, 3, 5, 7, 9):
        result = multiply(result, base)
    cache[exponent] = result
    return result
