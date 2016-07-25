from sieve import sieve

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
    # The only numbers ending with these digits that are prime
    if n == 2 or n == 5:
        return True
    # Avoid breaking on creating a sieve for 3**0.5 (too small)
    if n == 3:
        return True
    # Otherwise, these numbers cannot be prime
    if n % 10 in (0, 2, 4, 5, 6, 8):
        return False
    possible_factors = sieve(int(n**0.5))
    for factor in possible_factors:
        if n % factor == 0:
            return False
    return True
