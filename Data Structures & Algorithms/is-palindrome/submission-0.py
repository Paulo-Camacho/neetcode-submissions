class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        # let's build the alpha-numeric
        for curr in s:
            if curr.isalnum():
                arr.append(curr.lower())

        baz = arr[::-1]
        print(arr)
        return arr == baz
