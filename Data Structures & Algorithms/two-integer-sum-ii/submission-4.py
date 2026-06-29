# I know that I need to keep a counter of the sum and adjust the pointers from
# both ends of the given array I am just going to return an empty list if we 
# cannot find the indices
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        for curr in range(len(numbers)):
            track = numbers[left] + numbers[right]
            if track > target:
                right -= 1
                track = numbers[left] + numbers[right]
            
            elif track < target:
                left += 1
                track = numbers[left] + numbers[right]
            if track == target:
                return [left + 1, right + 1]
        return []




























        # # The idea is to have a sum
        # # have a left and right pointer* and moves each one 
        # # respective to if sum is < or > target
        # left = 0
        # right = len(numbers) - 1
        # while (left < right):
        #     ball = numbers[left] + numbers[right]
        #     if ball == target:
        #         return [left + 1, right + 1]
        #     if ball > target and left < right:
        #         right -= 1
        #         ball = numbers[left] + numbers[right]
        #     if ball < target and left < right:
        #         left += 1
        #         ball = numbers[left] + numbers[right]
            
        # return []

        







        # They want constant space so that means we need to
        # use two pointers on the orignal arr
        # One power to the input is that the information is sorted
        # What I think that means is that I can just start
        # by checking adjacent pairs first


        # # This only checks valid adjacent
        # for left in range(len(numbers) - 1):
        #     1right = left + 1
        #     if numbers[left] + numbers[right] == target:
        #         a_left = left + 1
        #         a_right = right + 1
        #         return [a_left, a_right]
            