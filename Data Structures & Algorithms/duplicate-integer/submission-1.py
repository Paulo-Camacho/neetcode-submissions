class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            seen.add(val)

        print(f'this is seen : {seen}')
        print(f'this is nums : {nums}')
        return not (len(nums) == len(seen))

        