class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # WINDOW METHOD
        # s="abcabcbb"
        l = 0
        largest = 0
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            largest = max(largest, r - l + 1)
        return largest