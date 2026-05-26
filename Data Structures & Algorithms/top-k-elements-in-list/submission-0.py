class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap
        # look at how many times memembers are visted and incremement
        # sort a list via recursion of hashmap
        # return said list

        hashy = {}

        for num in nums:
            if num in hashy:
                hashy[num] += 1
            else:
                hashy[num] = 1

        # notice how ! hashy.get(). We want it to be called later
        result = sorted(hashy, key = hashy.get, reverse=True)
        return result[:k]
        print(result)
        
