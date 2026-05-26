class Solution:

    def encode(self, strs: List[str]) -> str:
        long_str = ""
        # we are going to parse with num#word
        for word in strs:
            long_str += f'{len(word)}#{word}'
        
        print(long_str)
        return long_str

    def decode(self, s: str) -> List[str]:
#        5#Hello5#World
        left = 0
        arr = []
        while left < len(s):
            right = left 
            while s[right] != '#':
                right += 1
            # now we have the num saved
            num = s[left:right]
            # this should be right right length to capture the word
            word = s[right + 1 : right + 1 + int(num)]
            left = right + 1 + int(num)
            arr.append(word)
        print(arr)
        return arr






        
            


