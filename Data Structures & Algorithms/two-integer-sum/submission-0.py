class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums) - 1):
            left = nums[i]
            for j in range(i + 1, len(nums)):
                right = nums[j]
                if right + left == target:
                    arr += [i, j]
                    print(arr)
                    return arr
                
        return arr
        