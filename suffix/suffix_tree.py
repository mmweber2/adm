from bisect import bisect_left

class SuffixArray(object):
    """An array that keeps track of suffixes."""
    def __init__(self, s):
        """Create a new, sorted SuffixArray of string s.

        Suffixes are sorted using sorted(), so they are case sensitive:
        "None" is less than "none".

        If s is not a string, it will be converted to one with str().
        """
        s = str(s)
        self.array = sorted([s[i:] for i in xrange(len(s))])
        # Determine LCPs for each pair of (sorted) consecutive prefixes.
        # First item will have no common prefix because it has no predecessor.
        self.lcp = [0]
        for i in xrange(1, len(self.array)):
            prefix = SuffixArray._find_lcp(self.array[i], self.array[i-1])
            self.lcp.append(prefix)

    @staticmethod
    def _find_lcp(s1, s2):
        """Returns the length of the longest common prefix
        of strings s1 and s2.

        Returns 0 if there are no elements in common.
        Raises a TypeError if either or both elements are not strings.
        """
        # Comparisons and/or iterations might work with other types,
        # so check the types first.
        if not (isinstance(s1, str) and isinstance(s2, str)):
            raise TypeError
        # Put the shorter string first for ease of iteration.
        if len(s2) < len(s1):
            s1, s2 = s2, s1
        count = 0
        for i in xrange(len(s1)):
            if s1[i] == s2[i]:
              count += 1
            else: break
        return count

    # The bisect version works, but it might be making more comparisons
        # than are necessary.

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


    # TODO
    def longest_repeating(self):
        """Returns a list of all of the longest repeating substrings
        in this SuffixArray.

        If there are multiple repeating substrings that are all the
        maximum size, all are returned in a list. Otherwise, the list
        consists of the single longest repeating substring.

        Returns an empty list if the SuffixArray contains no repeating
        substrings.
        """
        # List of tuples of all max pairs
        max_pair = []
        max_size = 0
        # Get pair starting with the longest repeating string.
        for i in xrange(1, len(self.lcp)):
            pairs = self.lcp[i]
            if pairs > max_size:
                max_size = pairs
                # Reset max_pair, since a new size was found
                # We don't have to worry about i-1 at 0 because i's
                # value will always be 0 at index 0.
                max_pair = [self.array[i-1], self.array[i]]
            elif pairs == max_size:
                max_pair.append((self.array[i-1], self.array[i]))
        # Now that we have these pairs, figure out the longest repeating
        # List of all max-size repeating substrings (not tuples)
        all_max = []
        for pair in max_pair:
            print "Max size is ", max_size
            print "Max pair is ", max_pair
            shorter = pair[0]
            longer = pair[1]
            if len(pair[1]) < len(pair[0]):
                shorter = pair[1]
                longer = pair[0]
            for i in xrange(len(shorter)):
                if shorter[i] != longer[i]:
                all_max.append(shorter[:i])
        return all_max
