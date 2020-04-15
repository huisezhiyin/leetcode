class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])

        return longest
