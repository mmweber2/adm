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
    while digit < len(a.digits):
        # Reset carry for each new digit of a, since it will be appended
        # at the end of the previous digit
        carry = 0
        multiplicant = a.digits[-1 -digit]
        # Order of products doesn't matter, so insert at the beginning once
        # to allow simple 0-index lookup later
        products.insert(0, [])
        for i in xrange(len(b.digits)):
            product = multiplicant * b.digits[-1 -i]
            product += carry
            # Add smallest digit to list (to turn into final answer later)
            products[0].insert(0, product % 10)
            carry = product / 10
        # If carry is 0, it will be ignored when turning into a BigInteger
        products[0].insert(0, carry)
        # Add zeroes to adjust for position of multiplicant digit
        products[0].extend([0] * (digit))
        digit += 1
    result = BigInteger("0")
    for product in products:
        partial_result = BigInteger("".join([str(digit) for digit in product]))
        result = BigInteger.add(result, partial_result)
    if negative:
        return result._flip_sign()
    return result
