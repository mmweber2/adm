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
        multiplicant = a.digits[-1 - digit]
        for i in xrange(len(b.digits)):
            product = multiplicant * b.digits[-1 -i]
            # Don't bother adding zero products
            if product == 0: continue
            # Move the product over the correct number of zeroes
            zeroes = "0" * (i + digit)
            products.append(BigInteger(str(product) + zeroes))
        digit += 1
    result = BigInteger("0")
    for product in products:
        result = BigInteger.add(result, product)
    # We could just modify the negative attribute for result, but that
    # feels like a bad practice
    if negative:
        return BigInteger("-" + "".join([str(x) for x in result.digits]))
    return result
