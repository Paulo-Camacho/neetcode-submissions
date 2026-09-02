class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        l = -1
        r = (len(nums) - 1)
        middle = int(r - l / 2)
        while(l < r and middle < len(nums)):
            print("ran once")
            print(middle)
            finger = nums[middle]
            if finger == target:
                return middle
            elif finger < target:
                print("finger < ran")
                l += 1
                middle += 1
            elif finger > target:
                print("finger > ran")
                r -= 1
                middle -= 1

            print(f'middle:{middle} finger:{finger} l:{l} r:{r}')
        return -1
                



            



        