def sieve(n):
    """Returns a list of all prime numbers between 2 and n (inclusive).

    Args:
        n: integer, the number up to which to find prime numbers.
        Must be greater than 1.

    Returns:
        A list of integer primes between 2 and n.

    Raises:
        ValueError: n is < 2.
    """
    if n < 2:
        raise ValueError("cannot search for primes < 2")
    possible_primes = range(2, n + 1)
    for i in xrange(2, int(n**0.5) + 1):
        # Don't check multiples of non-prime numbers
        # -2 index to account for skipping 0 and 1
        if possible_primes[i-2] is None:
            continue
        for j in xrange(i * 2, n + 1, i):
            possible_primes[j-2] = None
    return filter(None, possible_primes)
