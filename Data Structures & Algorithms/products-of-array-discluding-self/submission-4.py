class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force n^2
        # make prefix and suffix product functions
        # input: 1, 2, 4, 6
        # output:1, 2, 8, 48
        # The idea is to get answer[i] = prefix[i - 1] * suffix[i + 1]
        prefix = self.prefixProduct(nums)
        suffix = self.suffixProduct(nums)
        answer = []
        for i in range(len(nums)):
            if i > 0:
                left = prefix[i - 1]
            else:
                left = 1
            if i < len(nums) - 1:
                right = suffix[i + 1]
            else:
                right = 1
            product = left * right
            answer.append(product)
        print (answer)
        return (answer)

    def suffixProduct(self, arr):
        suffix = [0] * len(arr)
        suffix[-1] = arr[-1]
        # input: 1, 2, 4, 6
        for right in range(len(arr) - 2, -1, -1):
            suffix[right] = suffix[right + 1] * arr[right]
        print(f'suffix {suffix}')
        return(suffix)

    def prefixProduct(self, arr):
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for left in range(1, len(arr)):
            prefix[left] = prefix[left - 1] * arr[left]
        print(f'prefix {prefix}')
        return(prefix)
