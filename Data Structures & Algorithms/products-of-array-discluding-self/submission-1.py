class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets just do a brute force n^2 for now

        arr = []
        for left in range(len(nums)):
            product = 1
            for right in range(len(nums)):
                if left != right:
                    product *= nums[right]
            arr.append(product)
                
        return(arr)
        print(arr)

            
                


            
        