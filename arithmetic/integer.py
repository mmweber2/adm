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

        A leading negative is ignored if the number contains only zeroes, so
        a num of "-000" would have digits of [0, 0, 0] and a negative 
        attribute of False.

        Args:
            num: string, the number to convert into a BigInteger.
                Must be comprised of only integer digits and (optionally)
                a leading negative sign. Leading zeroes are permitted, but
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
        self.digits = [int(c) for c in num]

    @staticmethod
    def add(n1, n2):
        """Adds two BigIntegers and returns a new BigInteger of the sum."""
        # TODO: Handle negatives
        # Work with smaller number in the same position
        if len(n1.digits) <= len(n2.digits):
            num1 = n1.digits[:]
            num2 = n2.digits[:]
        else:
            num1 = n2.digits[:]
            num2 = n1.digits[:]
        # BigInteger accepts a string, so track the result in this format
        result = ""
        carry = 0
        while len(num1) > 0:
            d1, d2 = num1.pop(), num2.pop()
            if carry != 0:
                d1 += carry
            carry = (d1 + d2) / 10
            digit_sum = (d1 + d2) % 10
            result = str(digit_sum) + result
        # Be sure to add any leftover carry
        if carry != 0:
            result = str(carry) + result
        return BigInteger(result)
