class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We have to scan the array for the mini
        # Compute the area for given mini
        # area_pool = []

        max_area = 0
        for left in range(len(heights)):
            mini = heights[left]
            for right in range(left, len(heights)):
                # For this implementation we are calculating area immediately
                mini = min(mini, heights[right])
                # This gives total number of bars computed which
                width = right - left + 1
                area = mini * width
                max_area = max(max_area, area)
                # area_pool.append(max_area)
                # print(f'left value:{heights[left]} right value:{heights[right]} mini value:{mini} width{width} area:{area}')
        # print(f'area_pool{area_pool}')
        return max_area






















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