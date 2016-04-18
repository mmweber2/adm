from bisect import bisect_left

class SuffixArray(object):
    """An array that keeps track of suffixes."""
    def __init__(self, s):
        """Creates a new, sorted SuffixArray of the suffixes for string s.

        Suffixes are case sensitive.

        Args:
            s: The string from which to form the SuffixArray.
               If s is not a string, it will be converted to one with
               str(). Must be comprised of ASCII characters.

        Raises:
            TypeError: array is not an iterable, contains values other
            than strings, or contains values outside of the ASCII
        """
        s = str(s)
        self._array = sorted([s[i:] for i in xrange(len(s))])
        # Determine LCPs (longest common prefixes) for each pair of
        # (sorted) consecutive prefixes.
        # The first item will have no common prefix because it has no
        # predecessor.
        self._lcp = [0]
        for i in xrange(1, len(self._array)):
            prefix = SuffixArray._find_lcp(self._array[i], self._array[i-1])
            self._lcp.append(prefix)

    @staticmethod
    def _find_lcp(s1, s2):
        """Finds the length of the longest common prefix of s1 and s2.

        Args:
            s1, s2: The strings to evaluate.

        Returns:
            The length of the longest common prefix of s1 and 2, or
            0 if there are no elements in common.

        Raises:
            TypeError: s1 or s2 is not a string.
        """
        # Comparisons work with other non-string types, so check
        # the types first.
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

    def is_substring(self, sub):
        """Checks for a substring in this string.

        An empty string is considered a substring of any string.

        Args:
            sub: The substring to check for in this SuffixArray.

        Returns:
            True iff sub is a substring of the string used to create
            this SuffixArray. An empty string is considered a substring
            of any other string.
        """
        if sub == "":
            return True
        # Find where the substring would go if we were to add it
        start = bisect_left(self._array, sub)
        # Increment the last character of sub as little as possible
        # in order to find the first following non-prefix word
        # Example: 'cass' would be incremented to 'cast'
        increment_last_char = sub[:-1] + chr(ord(sub[-1]) + 1)
        end = bisect_left(self._array, increment_last_char)
        # If start < end, there is at least one suffix in s that
        # has sub as a prefix, which means that sub is a substring.
        return start < end

    def longest_repeating(self):
        """Find the longest repeating substring.

        Returns:
            A list of all of the longest repeating substrings
            in this SuffixArray.

            If there are multiple repeating substrings that are all the
            same (maximum) size, they are all returned in a list.
            Otherwise, the list consists of the single longest repeating
            substring.
            To compare characters, the default comparator is used and
            whitespace and punctuation are considered.

            Returns a list containing only an empty string if
            the SuffixArray contains no repeating substrings.
        """
        lrs = [""]
        # Start at 1 because lcp[0] is always 0.
        for i in xrange(1, len(self._lcp)):
            prefix_size = self._lcp[i]
            # If there are no repeating characters, we don't want to
            # return an empty string for every single character, just
            # [""].
            if prefix_size == 0:
                continue
            repeated_string = self._array[i][:prefix_size]
            if prefix_size > len(lrs[0]):
                # Reset lrs because a new size was found.
                lrs = [repeated_string]
            elif prefix_size == len(lrs[0]):
                # If we expected a lot of repeats, it would be better
                # to use a set as well.
                if repeated_string not in lrs:
                    lrs.append(repeated_string)
        return lrs
