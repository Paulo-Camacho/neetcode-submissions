class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        if len(nums) == 1 and nums[0] != target:
            return -1
        elif nums[0] == target:
            return 0
        while l <= r:
            mid = math.ceil(l + ((r - l) // 2))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l += 1
                r -= 1
            
        return -1