from bisect import bisect, bisect_left

class SuffixArray(object):
    """An array that keeps track of suffixes."""
    def __init__(self, s):
        """Create a new, sorted SuffixArray of string s.

        Suffixes are sorted using sorted(), so they are case sensitive:
        "None" is less than "none".

        If s is not a string, it will be converted to one with
        str().
        """
        s = str(s)
        self.array = sorted([s[i:] for i in xrange(len(s))])

    # TODO: Count substrings too?
    def is_substring(self, sub):
        """Returns True iff sub is a substring of the string in
        this SuffixArray.

        An empty string is considered a substring of any string.
        """
        if sub == "":
            return True
        # Find where the substring would go if we added it
        start = bisect_left(self.array, sub)
        # Increment the last character of sub as little as possible
        # in order to find the first following non-prefix word
        increment_last_char = sub[:-1] + chr(ord(sub[-1]) + 1)
        end = bisect_left(self.array, increment_last_char)
        # If start < end, there is at least one suffix in s that
        # has sub as a prefix, which means that sub is a substring.
        return start < end


    # TODO: Add more strings?
    # Track Longest Common Prefix?
