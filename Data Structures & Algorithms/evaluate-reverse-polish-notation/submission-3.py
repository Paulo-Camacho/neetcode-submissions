class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # REVERSE POLISH NOTATION
        # I think the key is that we push the results value back
        self.stack = []
        self.neuvo = 0
        for x, val in enumerate(tokens):
            if val in "+-*/":
                operator = val
                b = int(self.stack.pop())
                a = int(self.stack.pop())
                if operator == "+":
                    self.neuvo = a + b
                    self.stack.append(self.neuvo)
                elif operator == "-":
                    self.neuvo = a - b
                    self.stack.append(self.neuvo)
                elif operator == "*":
                    self.neuvo = a * b
                    self.stack.append(self.neuvo)
                elif operator == "/":
                    self.neuvo = int(a / b)
                    self.stack.append(self.neuvo)
            else:
                self.stack.append(val)
            
        return int(self.stack[-1])