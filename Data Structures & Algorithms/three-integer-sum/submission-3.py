class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        print(nums)
        stack = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                if nums[left] + nums[right] == -1 * nums[i]:
                    result = [nums[left], nums[right], nums[i]]
                    left += 1
                    right -= 1
                    if result not in stack:
                        stack.append(result)
                elif nums[left] + nums[right] > - 1 * nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < - 1 * nums[i]:
                    left += 1
        return stack
                    






# nums[left] + nums[right] == -nums[i]















        # stack = []
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 check = sorted([nums[i], nums[j], nums[k]])
        #                 if check not in stack:
        #                     stack.append(check)
                        
        # print(stack)
        # return stack 



        