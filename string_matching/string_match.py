from collections import defaultdict

def string_match(text, pattern):
    """Returns all starting indices in text where text and pattern match.

    This search is case sensitive and considers spaces and punctuation.

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

        pattern: string, the case sensitive text for which to search.
        
    Returns:
        A list of all indices of text at which pattern can be found.
            Returns an empty list if pattern is not a substring of text
            or if pattern is an empty string.
    """
    if pattern == "" or len(pattern) > len(text):
        return []
    bad_chars = _build_bad_character_table(pattern)
    general_table, special_table = _build_good_suffix_tables(pattern)
    # Indices where a match of pattern begins in text
    matches = []
    start_pos = 0
    # Line up pattern at 0, so end of pattern lies at end_pos in text
    end_pos = len(pattern) - 1
    # The position reached in pattern on the previous attempt (for Galil's rule)
    previous_pos = -1 
    while end_pos < len(text):
        pattern_pos = len(pattern) - 1
        # Attempt to match pattern to string
        while (pattern_pos >= 0 and end_pos > previous_pos and 
                text[end_pos] == pattern[pattern_pos]):
            pattern_pos -= 1
            end_pos -= 1
        # How many extra characters to move forward
        skip = 0
        if pattern_pos == -1 or end_pos == previous_pos:
            # Found a full match of pattern or a position we know matches
            matches.append(start_pos)
            if len(pattern) > 1:
                end_pos += len(pattern) - special_table[1]
        else:
            text_char = text[end_pos]
            bc_value = bad_chars[text_char][pattern_pos]
            bc_result = pattern_pos - bc_value if bc_value != -1 else -1
            if pattern_pos + 1 == len(pattern):
                # Mismatch at first character checked
                suffix_result = 0
            elif general_table[pattern_pos + 1] != -1:
                # Suffix appears elsewhere in pattern
                suffix_result = len(pattern) - general_table[pattern_pos + 1]
            else:
                # Suffix is not part of rest of pattern; must use special table
                suffix_result = len(pattern) - special_table[pattern_pos + 1]
            skip = max(bc_result, suffix_result)
            previous_pos = end_pos if skip >= pattern_pos else previous_pos
        # Always move forward at least 1
        start_pos += max(1, skip)
        end_pos = start_pos + len(pattern) - 1
    return matches

def _build_bad_character_table(pattern):
    """Creates a 'bad character rule' table for Boyer-Moore string searches."""
    # Return -1 for any character not in pattern
    table = defaultdict(lambda: defaultdict(lambda: -1))
    # Mapping: [Char][current index]: previous index of character in pattern 
    for i in xrange(1, len(pattern)):
        # Set lookup to the highest index below i that matches each character,
        # which is either the previous index or the table value for the previous
        # index
        for char in pattern:
            if pattern[i-1] == char:
                table[char][i] = i-1
            # Avoid adding -1 to the table for all the indices not present
            elif i-1 in table[char]:
                table[char][i] = table[char][i-1]
    return table
    
def _build_good_suffix_tables(pattern):
    """Creates 'good suffix rule' tables for Boyer-Moore string searches."""
    # L table; for the general case
    # Mapping: [index in pattern]: previous location of that suffix in pattern
    general_table = defaultdict(lambda: -1)
    for i in xrange(1, len(pattern)):
        # Look for pattern[i+1:] because the match stopped at [i]
        pattern_loc = pattern[:i].rfind(pattern[i+1:])
        # Don't include other substrings where the previous letter is the same,
        # because those will never match when this substring doesn't
        if pattern_loc != -1 and pattern[pattern_loc - 1] != pattern[i - 1]:
            general_table[i] = pattern_loc
    # H table; for when there is a match or when the L table returns -1
    # Mapping: [index in pattern]: length of the longest suffix starting at 
    # that index which is also a prefix of pattern
    special_table = defaultdict(int)
    for i in xrange(1, len(pattern)):
        for j in xrange(len(pattern), i, -1):
            if pattern.startswith(pattern[i:j]):
                special_table[i] = j - i
                break
    return general_table, special_table
