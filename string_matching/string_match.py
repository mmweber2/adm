from collections import defaultdict

def string_match(text, pattern):
    """Returns all starting indices in text where text and pattern match.

    Uses the Boyer-Moore algorithm with the Galil rule:
        Create a 'bad character rule' table and two 'good suffix rule' tables.
        Line up the beginning of pattern with the beginning of text, but compare
            from the end of pattern.
        For each character, get the data for that index from both the
            bad character rule table and good suffix rule tables.
        Re-align the pattern along the text, skipping indices as determined by
            the maximum of the results from the tables.

    Args:
        text: string, the full body of text to search for pattern.

        pattern: string, the text for which to search.
        
    Returns:
        A list of all indices at which pattern starts in text.
            Returns an empty list if pattern is not a substring of text.
    """
    bad_chars = _bad_character_table(pattern)
    general_table, special_table = _good_suffix_tables(pattern)
    # Indices where a match of pattern begins in text
    matches = []
    start_pos = 0
    # Line up pattern at i, so end of pattern lies at end_pos in text
    end_pos = len(pattern) - 1
    while end_pos < len(text):
        pattern_pos = len(pattern) - 1
        # Attempt to match pattern to string
        while pattern_pos >= 0 and text[end_pos] == pattern[pattern_pos]:
            pattern_pos -= 1
            end_pos -= 1
        if pattern_pos == -1:
            # Found a full match of pattern
            matches.append(start_pos)
            if len(pattern) > 1:
                end_pos += len(pattern) - special_table[1]
        else:
            # Bad character rule result
            text_char = text[end_pos]
            if pattern_pos not in bad_chars[text_char]:
                bc_result = -1
            else:
                bc_result = pattern_pos - bad_chars[text_char][pattern_pos]
            if pattern_pos + 1 == len(pattern):
                # Mismatch at first character checked
                suffix_result = 0
            elif general_table[pattern_pos + 1] == -1:
                # Suffix is not part of pattern
                suffix_result = len(pattern) - special_table[pattern_pos + 1]
            else:
                # Suffix appears elsewhere in pattern
                suffix_result = len(pattern) - general_table[pattern_pos + 1]
            skip = max(bc_result, suffix_result)
            start_pos += skip
        start_pos += 1
        end_pos = start_pos + len(pattern) - 1
    return matches

def _bad_character_table(pattern):
    """Creates a 'bad character rule' table for Boyer-Moore string searches."""
    table = defaultdict(dict)
    # Mapping: [Char][index in pattern]: first index of character in pattern 
    for i, c in enumerate(pattern):
        # Set lookup to the highest index below i that matches the character,
        # or -1 if it doesn't match (which is also rfind's default behavior)
        table[c][i] = pattern.rfind(c, 0, i)
        # We'd like to return -1 for any character not in the table, but
        # even if we initialize that for alphabet characters, we'd still get
        # errors when checking for spaces, punctuation, etc.
    return table
    
def _good_suffix_tables(pattern):
    """Creates 'good suffix rule' tables for Boyer-Moore string searches."""
    # L table; for the general case
    # Mapping: [index in pattern]: next location of that suffix in pattern
    general_table = [-1 for _ in xrange(len(pattern))]
    for i in xrange(1, len(pattern)):
        pattern_loc = pattern.rfind(pattern[i+1:])
        if pattern[pattern_loc - 1] != pattern[i - 1]:
            general_table[i] = pattern_loc
    # H table; for when there is a match or when the L table returns 0
    # Mapping: [index in pattern]: length of longest suffix from that index
    special_table = [-1 for _ in xrange(len(pattern))]
    for i in xrange(len(pattern)):
        for j in xrange(len(pattern) - 1, i, -1):
            if pattern.startswith(pattern[i:j]):
                special_table[i] = 1 - j - i
                break
    return general_table, special_table