class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1 
        #          0 1 2 3 4 5 target = 5
        # nums = [-1,0,2,4,6,8]
        # 6 len
        # nums=[-1,0,3,5,9,12] I want 9
        # 0 + (6-1) // 2 => mid => 3
        # 0 + (2 - 0) // 2 
        # 4 + (6 - 4) // 2 4+1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        while (low <= high):
            mid = low + (high - low) // 2
            print(f'mid: {mid}')
            if (nums[mid] == target):
                return mid 
            elif (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
        return -1