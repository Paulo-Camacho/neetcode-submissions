class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 11:11AM brute force again so I get the idea and can get the monotonic stack
        max_area = 0
        for left in range(len(heights)):
            # The left in range in here is to make sure we 'scoot' the right right hand after each iteration
            mini = heights[left] 
            for right in range(left, len(heights)):
                width = right - left + 1
                mini = min(heights[right], mini)
                area = width * mini
                max_area = max(area, max_area)
        print(max_area)
        return max_area

        