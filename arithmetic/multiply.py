from integer import BigInteger

def multiply(a, b):
    """Returns the product of BigIntegers a and b.
    
    Args:
        a, b: BigIntegers to multiply.
        
    Returns:
        A new BigInteger of the product of a and b.
    """
    negative = False
    if a.negative ^ b.negative: negative = True
    # Put shorter number first for consistency
    if len(a.digits) > len(b.digits): a, b = b, a
    digit = 0
    products = []
    carry = 0
    while digit < len(a.digits):
        multiplicant = a.digits[-1 -digit]
        products.append([])
        for i in xrange(len(b.digits)):
            product = multiplicant * b.digits[-1 -i]
            product += carry
            # Add smallest digit to list (to turn into final answer later)
            products[-1].insert(0, product % 10)
            carry = product / 10
        digit += 1
        # If carry is 0, it will be ignored when turning into a BigInteger
        products[-1].insert(0, carry)
        # Add zeroes to allow for position of multiplicant digit
        products[-1].extend([0] * (digit - 1))
    result = BigInteger("0")
    for product in products:
        partial_result = BigInteger("".join([str(digit) for digit in product]))
        result = BigInteger.add(result, partial_result)
    if negative:
        return result._flip_sign()
    return result
