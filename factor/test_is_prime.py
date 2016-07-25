from is_prime import is_prime

def test_negative():
    assert not is_prime(-5)

def test_zero():
    assert not is_prime(0)

def test_one():
    assert not is_prime(1)

def test_two():
    assert is_prime(2)

def test_single_factor():
    assert not is_prime(4)

def test_multi_factor():
    assert not is_prime(12)

def test_larger_prime():
    assert is_prime(17)

def test_large_range():
    count = 0
    for x in xrange(2, 101):
        if is_prime(x):
            count += 1
    assert count == 25

