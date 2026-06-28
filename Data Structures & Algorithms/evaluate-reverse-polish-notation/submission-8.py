class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # From what I have read max operands are two
        # A sudo recursive patterns allows for more complicated operations
        # However the base case is such that when a operand is found
        # Do the operation on the last two existing member is stack


        # Ill label is such that a b .... etc <--- b is the top of stack etc etc
        stack = []
        for curr in tokens:
            if curr not in '+-*/':
                clean = int(curr)
                stack.append(clean)
            elif stack and curr in '+-*/':
                b = int(stack.pop())
                a = int(stack.pop())
                if curr == '+':
                    result = a + b
                elif curr == '-':
                    result = a - b
                elif curr == '*':
                    result = a * b
                elif curr == '/':
                    result = int(a / b)
                stack.append(result)
        return stack[-1]
            

        
        



























        
        # # REVERSE POLISH NOTATION
        # # I think the key is that we push the results value back
        # self.stack = []
        # self.neuvo = 0
        # for x, val in enumerate(tokens):
        #     if val in "+-*/":
        #         operator = val
        #         b = int(self.stack.pop())
        #         a = int(self.stack.pop())
        #         if operator == "+":
        #             self.neuvo = a + b
        #             self.stack.append(self.neuvo)
        #         elif operator == "-":
        #             self.neuvo = a - b
        #             self.stack.append(self.neuvo)
        #         elif operator == "*":
        #             self.neuvo = a * b
        #             self.stack.append(self.neuvo)
        #         elif operator == "/":
        #             self.neuvo = int(a / b)
        #             self.stack.append(self.neuvo)
        #     else:
        #         self.stack.append(val)
            
        # return int(self.stack[-1])