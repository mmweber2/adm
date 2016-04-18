#!/usr/local/bin/python
# coding: utf-8
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
    assert a._array == ['est', 'st', 't', 'test']
    # Only 't' and 'test' have any prefixes in common
    assert a._lcp == [0, 0, 0, 1]

def test_create_longer_string_for_lcp():
    a = SuffixArray("cheesechase")
    # Prefixes should be:
    # "ase, chase, cheesechase, e, echase, eesechase, esechase, hase,
    # heesechase, se, sechase"
    assert a._lcp == [0, 0, 2, 0, 1, 1, 1, 0, 1, 0, 2]

def test_find_lcp_first_empty():
    assert SuffixArray._find_lcp("", "test") == 0

def test_find_lcp_second_empty():
    assert SuffixArray._find_lcp("test", "") == 0

def test_find_lcp_first_shorter():
    # Also covers the case where they are both the same length.
    assert SuffixArray._find_lcp("test", "testing") == 4

def test_find_lcp_second_shorter():
    assert SuffixArray._find_lcp("extraneous", "extra") == 5

def test_find_lcp_not_string():
    assert_raises(TypeError, SuffixArray._find_lcp, None, "test")

def test_find_lcp_no_common():
    assert SuffixArray._find_lcp("test", "case") == 0

def test_create_empty():
    a = SuffixArray('')
    assert a._array == []
    assert a._lcp == [0]

def test_create_non_string():
    a = SuffixArray(None)
    assert a._array == ['None', 'e', 'ne', 'one']

def test_longest_repeating_no_terminal():
    """Prefixes match, but not at the end of either substring."""
    a = SuffixArray("chase chasing")
    assert a.longest_repeating() == ["chas"]

def test_longest_repeating_no_repeat():
    a = SuffixArray("abcdefg")
    assert a.longest_repeating() == [""]

def test_longest_repeating_multiple_repeats():
    a = SuffixArray("raccoon@cat%bear$dog!cat*dog^fish")
    assert a.longest_repeating() == ["cat", "dog"]

def test_longest_repeating_same_word_more_than_twice():
    a = SuffixArray("our great times are going to be greatly great")
    assert a.longest_repeating() == [" great"]

def test_longest_repeating_two_terminal():
    """Substrings match at the end of both substrings."""
    a = SuffixArray("Taketakingpartaking")
    assert a.longest_repeating() == ["taking"]

def test_longest_repeating_one_terminal():
    """Substrings match at the end of one of the strings."""
    a = SuffixArray("cake and more cake")
    assert a.longest_repeating() == ["cake"]

def test_longest_repeating_spaces():
    s = ("This is a long string. It is so long that it wraps " +
            "over multiple lines.")
    a = SuffixArray(s)
    assert a.longest_repeating() == [" long "]

# TODO: Once sort is fully implemented, allow the constructor to call
# sort and check the finished array instead of calling sort() directly.
def test_sort_first_char():
    s = SuffixArray('fish')
    assert SuffixArray.sort(s._array) == ['fish', 'h', 'ish', 'sh']

def test_sort_single_char():
    assert SuffixArray.sort(['c', 'a', 'b']) == ['a', 'b', 'c']

def test_sort_multiple_char():
    s = SuffixArray('cheesecake')
    expected = ['ake', 'cake', 'cheesecake', 'e', 'ecake', 'eesecake',
        'esecake', 'heesecake', 'ke', 'secake']
    assert SuffixArray.sort(s._array) == expected

def test_sort_more_than_two_shared():
    pass

def test_sort_non_ASCII():
    assert_raises(TypeError, SuffixArray.sort, SuffixArray("違う")._array)

def test_sort_non_string_iterable():
    assert_raises(TypeError, SuffixArray.sort, [2, 1])

def test_sort_non_suffix_array_iterable():
    """This should still work, but performance will be worse."""
    s = "test string"
    pass

def test_sort_non_iterable():
    assert_raises(TypeError, SuffixArray.sort, 2)

