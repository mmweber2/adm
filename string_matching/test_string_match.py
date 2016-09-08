from string_match import string_match
from string_match import _build_bad_character_table
from string_match import _build_good_suffix_tables
from nose.tools import assert_equals
from collections import defaultdict

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
    table = _build_bad_character_table(pattern)
    c_table = defaultdict(lambda: -1)
    c_table.update(((1, 0), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)))
    assert_equals(table['c'], c_table)
    t_table = defaultdict(lambda: -1)
    t_table.update(((3, 2), (4, 3), (5, 4), (6, 5), (7, 5)))
    assert_equals(table['t'], t_table)
    g_table = defaultdict(lambda: -1)
    g_table[7] = 6
    assert_equals(table['g'], g_table)

def test_good_suffix_table_L():
    pattern = "anpanman"
    general, special = _build_good_suffix_tables(pattern)
    expected = defaultdict(lambda: -1)
    expected.update(((5, 3), (6, 4)))
    assert_equals(general, expected)

def test_good_suffix_table_H():
    pattern = "man to man"
    general, special = _build_good_suffix_tables(pattern)
    expected = defaultdict(int)
    expected[7] = 3
    assert_equals(special, expected)
