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
    pos = 0
    while pos < len(text):
        loc = text[pos:].find(pattern)
        if loc == -1:
            break
        expected.append(loc + pos)
        pos += loc + 1
    assert_equals(len(expected), 6)
    assert_equals(string_match("aaaaaaab", "aa"), expected)

def test_match_case_sensitive():
    text = "I never thought I'd talk to him again"
    pattern = "I"
    expected = []
    pos = 0
    while pos < len(text):
        loc = text[pos:].find(pattern)
        if loc == -1:
            break
        expected.append(loc + pos)
        pos += loc + 1
    assert_equals(len(expected), 2)
    assert_equals(string_match(text, pattern), expected)
