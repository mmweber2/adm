from integer import BigInteger
from multiply import multiply
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
    assert_equals(a.digits, [0, 0])

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
    assert_equals(a.digits, [0, 0, 3, 2])

def test_big_int_float():
    assert_raises(ValueError, BigInteger, "1.0")

def test_big_int_non_number():
    assert_raises(ValueError, BigInteger, "hello")

def test_big_int_middle_negative():
    assert_raises(ValueError, BigInteger, "19-1")

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
    b = BigInteger("18446744073709551616")
    result = BigInteger.add(a, b)
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
    assert_equals(multiply(2, 3), 6)

def test_multiply_different_lengths():
    assert_equals(multiply(1012, 35), 35420)

def test_multiply_zeroes():
    assert_equals(multiply(0, 10), 0)
    assert_equals(multiply(0, 0), 0)
    assert_equals(multiply(5, 0), 0)
    assert_equals(multiply(0, -5), 0)

def test_multiply_two_negative():
    assert_equals(multiply(-5, -3), 15)
    assert_equals(multiply(-2, 3), -6)
    assert_equals(multiply(2, -1), -2)

def test_multiply_large():
    # 2**64 is just beyond the bounds of int, so Python makes it a long
    assert_equals(multiply(2**64, 100), 1844674407370955161600)



