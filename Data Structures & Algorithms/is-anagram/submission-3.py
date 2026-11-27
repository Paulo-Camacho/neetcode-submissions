class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        saw = {}
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        for char in t:
            if char not in saw:
                saw[char] = 1
            else:
                saw[char] += 1
        print(saw)
        print(seen)
        return (saw == seen)

        


