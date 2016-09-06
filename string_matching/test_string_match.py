from string_match import string_match
from string_match import _bad_character_table
from string_match import _good_suffix_tables
from nose.tools import assert_equals

def test_match_not_substring():
    assert_equals(string_match("a", "b"), [])

def test_match_empty_text():
    assert_equals(string_match("", "a"), [])

def test_match_empty_pattern():
    assert_equals(string_match("abc", ""), [])

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

def test_match_near_matches():
    text = "anpanman"
    pattern = "tan"
    assert_equals(string_match(text, pattern), [])

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

def test_bad_char_table():
    pattern = "ccttttgc"
    table = _bad_character_table(pattern)
    assert_equals(table['c'], [-1, 0, 1, 1, 1, 1, 1, 1])
    assert_equals(table['t'], [-1, -1, -1, 2, 3, 4, 5, 5])
    assert_equals(table['g'], [-1, -1, -1, -1, -1, -1, -1, 6])

def test_good_suffix_table_L():
    pattern = "anpanman"
    general, special = _good_suffix_tables(pattern)
    assert_equals(general, [-1, -1, -1, -1, -1, 3, 4, -1])

def test_good_suffix_table_H():
    pattern = "man to man"
    general, special = _good_suffix_tables(pattern)
    assert_equals(special, [0, 0, 0, 0, 0, 0, 0, 3, 0, 0])
