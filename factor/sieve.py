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
    possible_primes = range(n + 1)
    # Allow 0-indexing by filtering non-prime initial numbers
    possible_primes[0] = None
    possible_primes[1] = None
    for i in xrange(2, int(n**0.5) + 1):
        # Don't check multiples of non-prime numbers
        if possible_primes[i] is None:
            continue
        for j in xrange(i * 2, n + 1, i):
            possible_primes[j] = None
    return filter(None, possible_primes)
