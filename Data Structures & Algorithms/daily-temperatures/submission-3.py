class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Answer array
        answer = [0] * len(temperatures)
        stack = []
        for curr in range(len(temperatures)):
            # Comparing curr against the top of values listed at the top of the stack
            # This is neat because we are using the stack to store indices and referencing through temperatures
            while stack and temperatures[curr] > temperatures[stack[-1]]:
                answer[stack[-1]] = curr - stack[-1]
                stack.pop()
            stack.append(curr)
        print(f'This is answer {answer}')
        return answer

















        # answer = [0] * len(temperatures)
        # stack = []

        # for curr in range(len(temperatures)):
        #     while stack and temperatures[curr] > temperatures[stack[-1]]:
        #         answer[stack[-1]] = curr - stack[-1]
        #         print(f'curr: {curr} stack:{stack}')
        #         stack.pop()
        #         print(f'curr: {curr} pop stack:{stack}')
        #     stack.append(curr)
        # return answer
            































            
        # Let's do brute force for right now just to get our brain warmed up 06-01-26 4:14PM
        # answer = []
        # for curr in range(len(temperatures)):
        #     curr_val = temperatures[left]
        #     self.diff = 0
        #     for right in range(curr + 1, len(temperatures)):
        #         right_val = temperatures[right]
        #         if right_val > curr_val:
        #             self.diff = right - curr
        #             break
        #     answer.append(self.diff)
        # print(answer)
        # return answer 
            
