class Solution:
    def isPalindrome(self, s: str) -> bool:
        # True two pointer uses o(1) space
        # This means using two pointers and not making a new arr
        # compare original arr with two pointers and skip junk
        # Move char when there is a match or isalnum somehow
        # Have a while loop for each hand
        left = 0
        right = len(s) - 1
        
        while (left < right):
            left_hand = s[left].lower()
            right_hand = s[right].lower()
            while not left_hand.isalnum() and left < right:
                left += 1
                left_hand = s[left].lower()
            while not right_hand.isalnum() and left < right:
                right -= 1
                right_hand = s[right].lower()
            if left_hand == right_hand:
                left += 1
                right -= 1
            else:
                return False
        return True

        # arr = []
        # # let's build the alpha-numeric
        # for curr in s:
        #     if curr.isalnum():
        #         arr.append(curr.lower())

        # baz = arr[::-1]
        # print(arr)
        # return arr == baz