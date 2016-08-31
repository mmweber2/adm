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
        

    """
    bad_chars = _bad_character_table(pattern)
    general_table, special_table = _good_suffix_tables(pattern)
    # Indices where a match of pattern begins in string
    matches = []
    start_pos = 0
    while start_pos < len(text) - len(pattern):
        # Line up pattern at i, so end of pattern lies at pos
        end_pos = start_pos + len(pattern) - 1
        # Attempt to match pattern to string
        partial_match = ""
        for i in xrange(len(pattern) - 1, -1, -1):
            text_char = text[i]
            pattern_char = pattern[i]
            if text_char == pattern_char:
                partial_match += text_char
            else:
                bad_char_result = bad_chars[text_char][i]
                good_suffix_result = general_table[end_pos]
                if good_suffix_result == 0:
                    good_suffix_result = special_table[end_pos]
                skip = max(bad_char_result, len(pattern) - good_suffix_result)
                start_pos += skip
                break
        else:
            # Fully matched pattern to part of string
            matches.append(start_pos)
        start_pos += 1


# When characters don't match, good suffix will always be 0, so we will take the result from bad character

# TODO: Should bad char return -1 or 0?
def _bad_character_table(pattern):
    """Creates a 'bad character rule' table for Boyer-Moore string searches."""
    table = defaultdict(dict)
    # Mapping: [Char][index in pattern]: first index of character in pattern 
    for i, c in enumerate(pattern):
        # Set lookup to the highest index below i that matches the character,
        # or -1 if it doesn't match (which is also rfind's default behavior)
        table[c][i] = pattern.rfind(c, 0, i)
    return table
    
def _good_suffix_tables(pattern):
    """Creates 'good suffix rule' tables for Boyer-Moore string searches."""
    # L table; for the general case
    # Mapping: [index in pattern]: next location of that suffix in pattern
    general_table = [0 for _ in xrange(len(pattern))]
    for i in xrange(1, len(pattern)):
        pattern_loc = pattern.rfind(pattern[i:-1], 1, i)
        if pattern[pattern_loc - 1] != pattern[i - 1]:
            general_table[i] = pattern_loc
    # H table; for when there is a match or when the L table returns 0
    # Mapping: [index in pattern]: length of longest suffix from that index
    special_table = [0 for _ in xrange(len(pattern))]
    for i in xrange(len(pattern)):
        for j in xrange(len(pattern) - 1, i, -1):
            if pattern.startswith(pattern[i:j]):
                h_table[i] = 1 - j - i
                break
    return general_table, special_table
