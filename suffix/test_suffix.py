from suffix_tree import SuffixArray
from nose.tools import assert_raises

# Black box

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

