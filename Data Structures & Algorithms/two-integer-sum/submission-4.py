class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setty = {}
        for i, v in enumerate(nums):
            comp = target - v
            # print(setty)
            # print(comp)
            # ill just make a hash set
            if v in setty:
                # print(f'setty[v]{setty[v]}, i{i}')
                return [setty[v], i] 
            else:
                setty[comp] = i
        