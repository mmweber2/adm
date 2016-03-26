from suffix_tree import SuffixArray
from nose.tools import assert_raises

# Black box

def test_is_substring_middle():
    a = SuffixArray("banana")
    assert a.is_substring("nan")

def test_is_substring_front():
    a = SuffixArray("string tests")
    assert a.is_substring("strin")

def test_is_substring_end():
    a = SuffixArray("chairs")
    assert a.is_substring("airs")

def test_is_substring_false():
    a = SuffixArray("test")
    assert not a.is_substring("tired")

def test_is_substring_false_incremented():
    a = SuffixArray("test")
    assert not a.is_substring("tet")

def test_is_substring_false_longer():
    a = SuffixArray("test")
    assert not a.is_substring("testing")

def test_is_substring_empty():
    """Since this function relies on the last character, try an
    empty string.
    """
    a = SuffixArray("test")
    assert a.is_substring("")

# White box

def test_create_string():
    a = SuffixArray("test")
    assert a.array == ['est', 'st', 't', 'test']

def test_create_empty():
    a = SuffixArray('')
    assert a.array == []

def test_create_non_string():
    a = SuffixArray(None)
    assert a.array == ['None', 'e', 'ne', 'one']

