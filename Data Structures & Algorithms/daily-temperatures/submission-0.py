class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Let's do brute force for right now just to get our brain warmed up 06-01-26 4:14PM

        answer = []
        for left in range(len(temperatures)):
            left_val = temperatures[left]
            self.diff = 0
            for right in range(left + 1, len(temperatures)):
                right_val = temperatures[right]
                if right_val > left_val:
                    self.diff = right - left
                    break
            answer.append(self.diff)
                
                




        print(answer)
        return answer 
            
            
