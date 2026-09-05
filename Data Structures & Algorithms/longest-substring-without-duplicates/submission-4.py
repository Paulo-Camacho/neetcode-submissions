class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # WINDOW METHOD
        # s="abcabcbb"
        l = 0
        biggest = 0 
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            biggest = max(biggest, r - l + 1)

        return biggest