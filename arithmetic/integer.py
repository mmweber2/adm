class BigInteger(object):
    """Represents a large (or small) integer."""

    def __init__(self, num):
        """Creates a new BigInteger from a string.

        Each BigInteger has the following attributes:
            digits: A list of integers representing this number.
                For example, the number 1250 would have a digits list of
                [1, 2, 5, 0]. The number -2 would have a digits list of
                [2].

            negative: A boolean that is True iff this number is negative.

        Args:
            num: string, the number to convert into a BigInteger.
                Must be comprised of only integer digits and (optionally)
                a leading negative sign.

        Raises:
            ValueError: num contains non-digit characters, other than a leading
                negative sign.
        """
        self.negative = False
        # Negative signs are only allowed at the beginning of the number
        if num[0] == "-":
            self.negative = True
            num = num[1:]
        self.digits = [int(c) for c in num]
