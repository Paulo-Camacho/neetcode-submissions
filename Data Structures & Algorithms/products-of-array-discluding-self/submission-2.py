class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force n^2
        # [1, 2, 4, 6]
        arr = []
        for left in range(len(nums)):
            product = 1
            for right in range(len(nums)):
                if left != right:
                    product *= nums[right]
            arr.append(product)

        print(arr)
        return(arr)

