class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        s = {} 
        for i, num in enumerate(nums):
            complement = target - num
            # print(f'num:{num} s:{s}')
            if num in s:
                return [s[num], i]
            else:
                s[complement] = i
        # print(s)