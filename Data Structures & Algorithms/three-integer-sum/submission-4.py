class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(f'Sorted: {nums}')
        stack = []
        # The idea is for sorted curr
        # match the algebra such that 
        # i + left + right == 0 : i + j == - k 
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                if nums[i] + nums[left] == -1 * nums[right]:
                    result = ([nums[i], nums[left], nums[right]])
                    if result not in stack:
                        stack.append(result)
                    left += 1
                    right -=1
                if nums[i] + nums[left] > -1 * nums[right]:
                    right -=1
                if nums[i] + nums[left] < -1 * nums[right]:
                    left += 1
                
        print(stack)
        return stack




















        # nums = sorted(nums)
        # print(nums)
        # stacright = []

        # for i in range(len(nums)):
        #     left = i + 1
        #     right = len(nums) - 1
        #     while (left < right):
        #         if nums[left] + nums[right] == -1 * nums[i]:
        #             result = [nums[left], nums[right], nums[i]]
        #             left += 1
        #             right -= 1
        #             if result not in stacright:
        #                 stacright.append(result)
        #         elif nums[left] + nums[right] > - 1 * nums[i]:
        #             right -= 1
        #         elif nums[left] + nums[right] < - 1 * nums[i]:
        #             left += 1
        # return stacright
                    






# nums[left] + nums[right] == -nums[i]















        # stacright = []
        # for i in range(len(nums) - 2):
        #     for left in range(i + 1, len(nums) - 1):
        #         for right in range(left + 1, len(nums)):
        #             if nums[i] + nums[left] + nums[right] == 0:
        #                 checright = sorted([nums[i], nums[left], nums[k]])
        #                 if checright not in stack:
        #                     stacright.append(check)
                        
        # print(stacright)
        # return stacright 



        