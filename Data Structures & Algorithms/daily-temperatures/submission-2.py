class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for curr in range(len(temperatures)):
            while stack and temperatures[curr] > temperatures[stack[-1]]:
                answer[stack[-1]] = curr - stack[-1]
                print(f'curr: {curr} stack:{stack}')
                stack.pop()
                print(f'curr: {curr} pop stack:{stack}')
            stack.append(curr)
        return answer
            
































        # answer = [0] * len(temperatures)
        # stack = []
        # # Start with an empty stack
        # for curr in range(len(temperatures)):
        #     while stack and temperatures[curr] > temperatures[stack[-1]]:
        #         # The answer at given day = the difference found
        #         answer[stack[-1]] = curr - stack[-1]
        #         stack.pop()
        #     stack.append(curr)
                
        #     # if temperatures[curr] > temperatures[stack[-1]]:
        #     #     answer[stack[-1]] = curr - stack[-1]
        #     #     # Once it has been solved we do not need it in the stack. This just appends
        #     #     stack.append(curr)
        #     # print(f'curr{curr} stack{stack}')

        # print(f'This is answer {answer}')
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
            
