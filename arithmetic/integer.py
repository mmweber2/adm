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

        A leading negative is ignored if the number contains only zeroes,
        and all non-significant zeroes are ignored. Therefore, a num of
        "-000" would have digits of [0] and a negative attribute of False.

        Args:
            num: string, the number to convert into a BigInteger.
                Must be comprised of only integer digits and (optionally)
                a leading negative sign. Leading zeroes will be ignored, but
                must follow the negative sign if the number contains one.

        Raises:
            ValueError: num contains non-digit characters, other than one
                leading negative sign.
        """
        self.negative = False
        # Negative signs are only allowed at the beginning of the number
        if num[0] == "-":
            num = num[1:]
            # Ignore negative sign if all digits are zeroes
            if set(num) != set("0"):
                self.negative = True
        # Check for all zeroes again now that leading negative is removed
        if set(num) == set("0"):
            self.digits = [0]
            return
        # Ignore all leading zeroes
        while num[0] == "0":
            num = num[1:]
        self.digits = [int(c) for c in num]

    def __cmp__(self, other):
        """Compares two BigInteger objects."""
        # Returns 1 if self > other, 0 if self == other, and -1 if self < other
        # Check for opposing signs
        if self.negative:
            if other.negative is False: return -1
        elif other.negative: return 1
        # Same signs, compare lengths
        if len(self.digits) < len(other.digits):
            return 1 if self.negative else -1
        if len(other.digits) < len(self.digits):
            return -1 if self.negative else 1
        # Same sign and same length
        for i in xrange(len(self.digits)):
            if self.digits[i] > other.digits[i]:
                return 1
            if self.digits[i] < other.digits[i]:
                return -1
        # Numbers are the same length and all digits are equal
        return 0
 
    @staticmethod
    def add(n1, n2):
        """Adds two BigIntegers and returns a new BigInteger of the sum.

        This function currently does not fully support negative numbers.
        Negative BigIntegers may be used as input, but their result will
        be inaccurate if only one of the numbers is negative.
        If both n1 and n2 have the same sign, the result will be correct
        and have that sign as well.
        Zero is considered positive for these functions, so a negative
        number added to zero will give an incorrect result.

        Args:
            n1, n2: BigIntegers to sum.

        Returns:
            A new BigInteger representing the sum.
        """
        # TODO: Handle negatives
        # Work with smaller number in the same position
        if n1 < n2:
            num1, num2 = n1.digits[:], n2.digits[:]
        else:
            num1, num2 = n2.digits[:], n1.digits[:]
        # BigInteger accepts a string, so track the result in this format
        result = ""
        carry = 0
        while len(num1) > 0:
            d1, d2 = num1.pop(), num2.pop()
            # This might cause d1 to become multi-digit, but the mod
            # and division results will still be accurate
            if carry != 0:
                d1 += carry
            carry = (d1 + d2) / 10
            digit_sum = (d1 + d2) % 10
            result = str(digit_sum) + result
        # We may be left with leftover num2 and/or a carry
        while carry != 0 and len(num2) > 0:
            d2 = num2.pop()
            digit_sum = (carry + d2) % 10
            carry = (carry + d2) / 10
            result = str(digit_sum) + result
        # If carry runs out before num2
        result = "".join([str(x) for x in num2]) + result
        # If there is still a carry after both numbers have run out
        if carry != 0:
            result = str(carry) + result
        # Result is negative only if both are negative, since
        # adding mixed sign numbers is currently not supported
        if n1.negative and n2.negative:
            return BigInteger("-" + result)
        return BigInteger(result)
