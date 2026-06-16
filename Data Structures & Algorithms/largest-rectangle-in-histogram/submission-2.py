class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        for left in range(len(heights)):
            mini = heights[left]
            for right in range(left, len(heights)):
                # We start checking from our left pointer and keep scanning until we find a new mini
                mini = min(mini, heights[right])
                width = right - left + 1
                area = width * mini
                max_area = max(area, max_area)
        
        return max_area






































        # # We have to scan the array for the mini
        # # Compute the area for given mini
        # area_pool = []
        # for left in range(len(heights)):
        #     max_area = 0
        #     mini = heights[left]
        #     for right in range(left, len(heights)):
        #         # For this implementation we are calculating area immediately
        #         mini = min(mini, heights[right])
        #         # This gives total number of bars computed which
        #         width = right - left + 1
        #         area = mini * width
        #         max_area = max(max_area, area)
        #         area_pool.append(max_area)
        #         # print(f'left value:{heights[left]} right value:{heights[right]} mini value:{mini} width{width} area:{area}')
        # # print(f'area_pool{area_pool}')
        # return max(area_pool)


        # Let me sum up what the brute force method does
        # for each left we declare and scan each right for the smallest value of rectangle
        # with the syntax of right - left + 1 this will always yeild the number of total bar width
        # we then take the max continous area via mini * width 
        # we use the built in max function to compare the max against the new max and append to max_area
        






















        # Iterate through entire array
        # Push the duplicate and find the max duplicates
        # Then just add number of duplicates against the height of that bar
        # This seems to easy I am propbably missing something herek
        # heights = sorted(heights, reverse=True)
        # stack = []
        # stack.append(heights[0])
        # for curr in range(1, len(heights) - 1):
        #     if heights[curr] == stack[-1]:
        #         stack.append(heights[curr])
        # area = stack[-1] + len(stack) - 1

        # print(f'Stack: {stack}')
        # print(f'Area: {area}')
        # return area