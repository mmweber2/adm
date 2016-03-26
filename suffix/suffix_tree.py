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

    # TODO: Add more strings?
    # Track Longest Common Prefix?
