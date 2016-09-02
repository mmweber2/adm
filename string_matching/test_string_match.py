from string_match import string_match
from nose.tools import assert_equals

def test_match_not_substring():
    assert_equals(string_match("a", "b"), [])

def test_match_end_of_string():
    expected = ["cheesecake".find("cake")]
    assert_equals(string_match("cheesecake", "cake"), expected)

def test_match_beginning_of_string():
    assert_equals(string_match("ab", "a"), [0])

def test_match_multiple_matches():
    text = "aaaaaaab"
    pattern = "aa"
    expected = []
    for i in xrange(len(text)):
        loc = text[i:].find(pattern)
        if loc > -1:
            expected.append(loc + i)
    assert_equals(string_match("aaaaaaab", "aa"), expected)

