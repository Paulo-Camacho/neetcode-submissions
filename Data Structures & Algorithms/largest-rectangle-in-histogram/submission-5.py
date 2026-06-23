class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        # The top of the stack will represent the smaller bar while extending the current bar
        max_area = 0
        stack = []
        for curr in range(len(heights)):
            while stack and heights[stack[-1]] > heights[curr]:
                # Current bar that we are on
                height = heights[stack[-1]]
                stack.pop()
                # If the stack is empty we know the the 'left' boundry is -1
                if not stack:
                    left = -1
                else:
                # The left boundry is the location of the most recent unresolved bar
                    left = stack[-1]
                width = curr - left - 1
                area = width * height
                max_area = max(area, max_area)
            stack.append(curr)
            

        while stack:
            height = heights[stack[-1]]
            stack.pop()
            # If the stack is empty we know the the 'left' boundry is -1
            if not stack:
                left = -1
            else:
            # The left boundry is the location of the most recent unresolved bar
                left = stack[-1]
            right = len(heights)
            width = right - left - 1
            area = width * height
            max_area = max(area, max_area)

        return max_area


            
            





















        # # 11:11AM brute force again so I get the idea and can get the monotonic stack
        # max_area = 0
        # for left in range(len(heights)):
        #     # The left in range in here is to make sure we 'scoot' the right right hand after each iteration
        #     mini = heights[left] 
        #     for right in range(left, len(heights)):
        #         width = right - left + 1
        #         mini = min(heights[right], mini)
        #         area = width * mini
        #         max_area = max(area, max_area)
        # print(max_area)
        # return max_area

        