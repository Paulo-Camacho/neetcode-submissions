class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Remeber the idea of binary search is to move the bounderies given if the target is larger or smaller
        # Moving the bounderies in such a way that we get rid of half of the unused data
        # [0, 2] 2
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = int((l + r) / 2)
            finger = nums[mid]
            if finger == target:
                return mid
            elif finger < target:
                l = mid + 1
            elif finger > target:
                r = mid - 1
                
        return -1

