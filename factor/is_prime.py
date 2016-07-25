from factorize import factorize

def is_prime(n):
    """Returns whether n is a prime number.

    Returns False for any negative numbers, 0, and 1.

    Args:
        n: integer, the number to check for primality.

    Returns:
        True iff n is a prime number.
    """
    if n < 2:
        return False
    primes = factorize(n)
    # Checking for a single prime doesn't work for squared numbers (such as 9),
    # so check that the last (only) prime is actually n itself.
    return primes[-1] == n


