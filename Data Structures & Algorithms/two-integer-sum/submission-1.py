class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The idea is that you compute the complement if complement is inside of set return said complement if not just add ith element to the set


        uni = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in uni:
                return [uni[complement], i]
            else:
                uni[nums[i]] = i
