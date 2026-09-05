class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # starting to solve with window method
        # s="abcabcbb"
        l = 0
        window = ""
        largest = 0
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            largest = max(largest, r - l + 1)
            
        print(largest)
        return largest

