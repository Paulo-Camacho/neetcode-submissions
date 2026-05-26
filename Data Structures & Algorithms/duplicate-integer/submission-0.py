class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            check.add(nums[i])

        if len(nums) != len(check):
            return True
        elif len(nums) == len(check):
            return False
        

        