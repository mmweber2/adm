from integer import BigInteger
from multiply import multiply
from divide import divide
from power import power
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_big_int_normal():
    a = BigInteger("2502")
    assert_equals(a.digits, [2, 5, 0, 2])
    assert a.negative is False

def test_big_int_zeroes():
    a = BigInteger("0")
    assert_equals(a.digits, [0])
    assert a.negative is False
    a = BigInteger("00")
    assert_equals(a.digits, [0])

def test_big_int_negative_zero():
    a = BigInteger("-0")
    assert_equals(a.digits, [0])
    assert a.negative is False

def test_big_int_negative_int():
    a = BigInteger("-100")
    assert_equals(a.digits, [1, 0, 0])
    assert a.negative is True

def test_big_int_large_number():
    a = BigInteger("18446744073709551616")
    digit_list = [1, 8, 4, 4, 6, 7, 4, 4, 0, 7, 3, 7, 0, 9, 5, 5, 1, 6, 1, 6]
    assert_equals(a.digits, digit_list)

def test_big_int_leading_zeroes():
    a = BigInteger("0032")
    assert_equals(a.digits, [3, 2])

def test_big_int_float():
    assert_raises(ValueError, BigInteger, "1.0")

def test_big_int_non_number():
    assert_raises(ValueError, BigInteger, "hello")

def test_big_int_middle_negative():
    assert_raises(ValueError, BigInteger, "19-1")

# Tests for __cmp__

def test_cmp_both_pos_one_longer():
    a = BigInteger("2502")
    b = BigInteger("35")
    assert a > b

def test_cmp_zeroes():
    a = BigInteger("0")
    b = BigInteger("2")
    c = BigInteger("-30")
    assert a < b
    assert a > c
    assert b > c

def test_cmp_both_negative():
    a = BigInteger("-5")
    b = BigInteger("-22")
    assert a > b

def test_cmp_longer_negative():
    a = BigInteger("-100")
    b = BigInteger("3")
    assert a < b

def test_cmp_same_size():
    a = BigInteger("25")
    b = BigInteger("31")
    assert a < b

def test_cmp_equal():
    a = BigInteger("32")
    b = BigInteger("32")
    assert a == b

# Tests for _flip_sign

def test_flip_sign_pos_neg():
    a = BigInteger("1")
    assert_equals(a._flip_sign(), BigInteger("-1"))

def test_flip_sign_neg_pos():
    a = BigInteger("-1")
    assert_equals(a._flip_sign(), BigInteger("1"))

# Tests for _clone

def test_clone_positive():
    a = BigInteger("25")
    assert_equals(a._clone_digits(), a)

def test_clone_negative():
    a = BigInteger("-3")
    assert_equals(a._clone_digits(), BigInteger("3"))

# Tests for BigInteger.add

def test_add_two_single():
    result = BigInteger.add(BigInteger("1"), BigInteger("2"))
    assert_equals(result.digits, [3])
    assert result.negative is False

def test_add_same_number():
    a = BigInteger("15")
    result = BigInteger.add(a, a)
    assert_equals(result.digits, [3, 0])

def test_add_single_with_carry():
    result = BigInteger.add(BigInteger("5"), BigInteger("7"))
    assert_equals(result.digits, [1, 2])

def test_add_zeroes():
    result = BigInteger.add(BigInteger("0"), BigInteger("2"))
    assert_equals(result.digits, [2])
    result = BigInteger.add(BigInteger("1"), BigInteger("0"))
    assert_equals(result.digits, [1])
    result = BigInteger.add(BigInteger("0"), BigInteger("0"))
    assert_equals(result.digits, [0])

def test_add_two_long():
    a = BigInteger("18446744073709551616")
    result = BigInteger.add(a, a)
    expected =  [3, 6, 8, 9, 3, 4, 8, 8, 1, 4, 7, 4, 1, 9, 1, 0, 3, 2, 3, 2]
    assert_equals(result.digits, expected)

def test_add_different_lengths():
    result = BigInteger.add(BigInteger("1"), BigInteger("721"))
    assert_equals(result.digits, [7, 2, 2])
    result = BigInteger.add(BigInteger("489"), BigInteger("12"))
    assert_equals(result.digits, [5, 0, 1])

def test_add_negatives():
    result = BigInteger.add(BigInteger("2"), BigInteger("-5"))
    assert_equals(result.digits, [3])
    assert result.negative is True
    result = BigInteger.add(BigInteger("-3"), BigInteger("6"))
    assert_equals(result.digits, [3])
    assert result.negative is False
    result = BigInteger.add(BigInteger("-3"), BigInteger("-6"))
    assert_equals(result.digits, [9])
    assert result.negative is True
    result = BigInteger.add(BigInteger("-2"), BigInteger("0"))
    assert_equals(result.digits, [2])
    assert result.negative is True

# Multiply tests

def test_multiply_small_numbers():
    a = BigInteger("2")
    b = BigInteger("3")
    assert_equals(multiply(a, b).digits, [6])

def test_multiply_different_lengths():
    a = BigInteger("1012")
    b = BigInteger("35")
    assert_equals(multiply(a, b).digits, [3, 5, 4, 2, 0])

def test_multiply_zeroes():
    a = BigInteger("0")
    assert_equals(multiply(a, BigInteger("10")).digits, [0])
    assert_equals(multiply(a, a).digits, [0])
    assert_equals(multiply(BigInteger("5"), a).digits, [0])
    assert_equals(multiply(a, BigInteger("-5")).digits, [0])

def test_multiply_two_negative():
    assert_equals(multiply(BigInteger("-5"), BigInteger("-3")).digits, [1,5])
    result = multiply(BigInteger("-2"), BigInteger("3"))
    assert_equals(result.digits, [6])
    assert result.negative
    result = multiply(BigInteger("2"), BigInteger("-1"))
    assert_equals(result.digits, [2])
    assert result.negative

def test_multiply_carry():
    a = BigInteger("12")
    b = BigInteger("56")
    expected = BigInteger("672")
    assert_equals(multiply(a, b), expected)

def test_multiply_one_large():
    # 2**64 is just beyond the bounds of int, so Python makes it a long
    a = BigInteger("18446744073709551616")
    expect = [1, 8, 4, 4, 6, 7, 4, 4, 0, 7, 3, 7, 0, 9, 5, 5, 1, 6, 1, 6, 0, 0]
    assert_equals(multiply(a, BigInteger("100")).digits, expect)

def test_multiply_two_large():
    a = BigInteger("48446744073709551616")
    b = BigInteger("130808823666624465123")
    expected = BigInteger("6337261602759956545834207900472160288768")
    assert_equals(multiply(a, b), expected)

# Subtract tests

def test_subtract_zeroes():
    a = BigInteger("0")
    assert_equals(BigInteger.subtract(a, a), a)
    assert_equals(BigInteger.subtract(BigInteger("1"), a).digits, [1])
    assert_equals(BigInteger.subtract(a, BigInteger("5")), BigInteger("-5"))
    result = BigInteger.subtract(a, BigInteger("-2"))
    assert_equals(result, BigInteger("2"))

def test_subtract_from_negative():
    result = BigInteger.subtract(BigInteger("-1"), BigInteger("2"))
    assert_equals(result, BigInteger("-3"))
    result = BigInteger.subtract(BigInteger("-1"), BigInteger("-2"))
    assert_equals(result, BigInteger("1"))

def test_subtract_positive_same_number_digits_positive():
    # Same number of digits, positive result
    result = BigInteger.subtract(BigInteger("5"), BigInteger("1"))
    assert_equals(result, BigInteger("4"))

def test_subtract_positive_same_number_digits_negative():
    # Same number of digits, negative result
    result = BigInteger.subtract(BigInteger("1"), BigInteger("5"))
    assert_equals(result, BigInteger("-4"))

def test_subtract_positive_same_number():
    # Same number
    result = BigInteger.subtract(BigInteger("3"), BigInteger("3"))
    assert_equals(result, BigInteger("0"))

def test_subtract_positive_smaller_minuend():
    # Second number has more digits
    c = BigInteger("2")
    d = BigInteger("12")
    assert_equals(BigInteger.subtract(c, d), BigInteger("-10"))

def test_subtract_positive_no_carry():
    # First number has more digits (no carry)
    d = BigInteger("12")
    c = BigInteger("2")
    assert_equals(BigInteger.subtract(d, c), BigInteger("10"))

def test_subtract_positive_single_digit_carry():
    # Requires a carry
    result = BigInteger.subtract(BigInteger("10"), BigInteger("1"))
    assert_equals(result, BigInteger("9"))

def test_subtract_positive_multi_digit_carry():
    # Requires a multi-digit carry
    result = BigInteger.subtract(BigInteger("100"), BigInteger("2"))
    assert_equals(result, BigInteger("98"))

def test_subtract_positive_later_digit_carry():
    # Requires a carry later than the first digit
    result = BigInteger.subtract(BigInteger("115"), BigInteger("20"))
    assert_equals(result, BigInteger("95"))

def test_subtract_positive_large():
    a = BigInteger("48446744073709551616")
    b = BigInteger("24501785728478724121")
    result = BigInteger.subtract(a, b)
    expected = BigInteger("23944958345230827495")
    assert_equals(result, expected)

# Divide tests

def test_divide_int_result_positive():
    result = divide(BigInteger("3"), BigInteger("1"))
    assert_equals(result, BigInteger("3"))

def test_divide_remainder_result_positive():
    result = divide(BigInteger("3"), BigInteger("2"))
    assert_equals(result, BigInteger("1"))

def test_divide_positive_multi_digit():
    result = divide(BigInteger("30"), BigInteger("2"))
    assert_equals(result, BigInteger("15"))

def test_divide_remainder_result_negative():
    result = divide(BigInteger("-3"), BigInteger("2"))
    assert_equals(result, BigInteger("-1"))
    result = divide(BigInteger("3"), BigInteger("-2"))
    assert_equals(result, BigInteger("-1"))

def test_divide_smaller_dividend():
    result = divide(BigInteger("3"), BigInteger("5"))
    assert_equals(result, BigInteger("0"))

def test_divide_by_zero():
    assert_raises(ZeroDivisionError, divide, BigInteger("2"), BigInteger("0"))

def test_divide_large():
    a = BigInteger("96893488157419103232")
    b = BigInteger("48446744073709551616")
    result = divide(a, b)
    assert_equals(result, BigInteger("2"))

# Power (exponent) tests

def test_power_even_exponent():
    result = power(BigInteger("3"), BigInteger("2"))
    assert_equals(result, BigInteger("9"))

def test_power_odd_exponent():
    result = power(BigInteger("2"), BigInteger("3"))
    assert_equals(result, BigInteger("8"))

def test_power_zero_base():
    result = power(BigInteger("0"), BigInteger("3"))
    assert_equals(result, BigInteger("0"))
    
def test_power_zero_exponent():
    result = power(BigInteger("2"), BigInteger("0"))
    assert_equals(result, BigInteger("1"))

def test_power_one_exponent():
    result = power(BigInteger("3"), BigInteger("1"))
    assert_equals(result, BigInteger("3"))

def test_power_large():
    a = BigInteger("48446744073709551616")
    result = power(a, BigInteger("2"))
    assert_equals(result, BigInteger("2347087011343511560423374607431768211456"))

def test_power_negative_base_even():
    result = power(BigInteger("-2"), BigInteger("4"))
    assert_equals(result, BigInteger("16"))

def test_power_negative_base_odd():
    result = power(BigInteger("-3"), BigInteger("3"))
    assert_equals(result, BigInteger("-27"))

def test_power_negative_exponent():
    assert_equals(power(BigInteger("3"), BigInteger("-2")), BigInteger("0"))


