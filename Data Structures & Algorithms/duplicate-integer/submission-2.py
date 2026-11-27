class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni = set()
        for num in nums:
            if num in uni:
                return True 
            else:
                uni.add(num)
        return False

        