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
        if num[0] == "0":
            zero_index = 0
            while num[zero_index + 1] == "0":
                zero_index += 1
            num = num[zero_index+1:]
        self.digits = [int(c) for c in num]

    def __repr__(self):
        """Represents this BigInteger as a string."""
        digits = "".join([str(x) for x in self.digits])
        return "-" + digits if self.negative else digits

    def _clone_digits(self):
        """Returns a positive clone of this BigInteger."""
        # Copy digits over all at once instead of converting to string first
        clone = BigInteger("0")
        clone.digits = self.digits
        return clone

    def _flip_sign(self):
        """Returns a new BigInteger with the same value but opposite sign."""
        number = "".join([str(x) for x in self.digits])
        if self.negative:
            return BigInteger(number)
        # The constructor won't allow -0, so calling this function with a
        # zero BigInteger will just create a copy of that BigInteger.
        return BigInteger("-" + number)

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

        Args:
            n1, n2: BigIntegers to sum.

        Returns:
            A new BigInteger representing the sum.
        """
        if n1.negative ^ n2.negative:
            negative_int, positive_int = (n1, n2) if n1.negative else (n2, n1)
            negative_int = negative_int._flip_sign()
            return BigInteger.subtract(positive_int, negative_int)
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

    @staticmethod
    def subtract(n1, n2):
        """Subtracts one BigInteger from another and returns the difference.

        Note that neither of the original BigIntegers are modified after
        this operation.

        Args:
            n1, n2: BigIntegers to subtract. n1 is the minuend and
            n2 is the subtrahend, so the result will be n1 - n2.

        Returns:
            A new BigInteger representing the difference of n1 and n2.
        """
        # a - b = a + (-b) if b is negative
        if n2.negative:
            return BigInteger.add(n1, n2._flip_sign())
        if n1.negative: # and n2 is not
            # Add both numbers as if positive, then flip signs accordingly
            return BigInteger.add(n1._flip_sign(), n2)._flip_sign()
        # a - b = -(b - a)
        if n2 > n1:
            return BigInteger.subtract(n2, n1)._flip_sign()
        result = ""
        # Make copy of n1 so we can modify it for carries
        n1_digits = n1.digits[:]
        for i in xrange(len(n2.digits)):
            digit_difference = n1_digits[-1 - i] - n2.digits[-1 -i]
            # Is there another digit to carry from?
            if digit_difference < 0 and len(n1_digits) > i + 1:
                # Start at the digit to the left and check for non-zeroes
                start = len(n1_digits) - 2 - i
                for j in xrange(start, -1, -1):
                    if n1_digits[j] > 0:
                        # Turn any digits between j and start j into 9s
                        n1_digits[j] -= 1
                        for carried in xrange(j+1, start+1):
                            n1_digits[carried] = 9
                        # Carry means borrowing 10 from the next digit
                        result = str(10 + digit_difference) + result
                        break
            else:
                result += str(digit_difference)
        if len(n1_digits) > len(n2.digits):
            size_diff = len(n1_digits) - len(n2.digits)
            remaining_digits = [str(x) for x in n1_digits[:size_diff]]
            result = "".join(remaining_digits) + result
        return BigInteger(result)
