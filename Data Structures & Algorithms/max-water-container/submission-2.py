class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) time and O(1) space
        # moving only the side that limits the area
        # This means moving only the side that is smaller
        # We might only need a while loop for this
        # I say let's store the max area of two given pillars then move the limit
        max_area = 0
        left = 0
        right = len(heights) - 1
        while (left < right):
            width = right - left
            curr_height = min(heights[left], heights[right])
            area = width * curr_height
            max_area = max(max_area, area)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        print(max_area)
        return(max_area)
            







       # Interesting 
       # Brute force was be calculating total area
       # each time
       # I am always ensured an input of at least 2


       # area would be L*H height would be bounded by lower one
       # width = end - current + 1
       # Let's start with brute force

        # max_area = 0
        # for left in range(len(heights)):
        #     for right in range(left + 1, len(heights)):
        #         width = right - left  
        #         # Height can never be higher than heights[left]
        #         # The brute-force method is surprisingly simple
        #         # The big key is when making a valid bucket only the smallest one is valid 
        #         # valid height * width
        #         max_height = min(heights[left], heights[right])
        #         area = max_height * width
        #         max_area = max(max_area, area)
        #         # print(f'heights[left]:{heights[left]} heights[right:{heights[right]}')
        #         # print(f'max_height:{max_height}')
        #         # print(f'area:{area} max_area:{max_area}')

        # print(max_area)
        # return max_area
            
