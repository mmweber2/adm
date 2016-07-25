from sieve import sieve

def factorize(p):
    """Returns a list of the prime factors of p.

    If p is itself prime, returns a list consisting of one element, p.

    Args:
        p: integer, the number for which to find prime factors.

    Returns:
        A list of the prime factors for p, or an empty list if p < 2.
    """
    primes = sieve(p)
    # If p is prime, it should be at the end of the list and will have
    # no other factors
    if primes[-1] == p:
        return [p]
    factors = []
    for prime in primes:
        if p == 1:
            break
        if p % prime == 0:
            factors.append(prime)
            p /= prime
    return factors
