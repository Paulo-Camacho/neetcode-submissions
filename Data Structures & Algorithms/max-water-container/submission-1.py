class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # Interesting 
       # Brute force was be calculating total area
       # each time
       # I am always ensured an input of at least 2


       # area would be L*H height would be bounded by lower one
       # width = end - current + 1
       # Let's start with brute force

        max_area = 0
        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                width = right - left  
                # Height can never be higher than heights[left]
                max_height = min(heights[left], heights[right])
                area = max_height * width
                max_area = max(max_area, area)
                # print(f'heights[left]:{heights[left]} heights[right:{heights[right]}')
                # print(f'max_height:{max_height}')
                # print(f'area:{area} max_area:{max_area}')

        print(max_area)
        return max_area
            
