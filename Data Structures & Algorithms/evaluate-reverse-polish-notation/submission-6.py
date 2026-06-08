class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # The idea is to have a stack the pushes the numbers
        # Then when met with operand operator and push result onto stack
        stack = []
        for i, curr in enumerate(tokens):
            print(f'This is i: {i} curr: {curr}')
            if curr in "+-*/":
                print(f"i: {i}, curr: {stack}")
                a = int(stack.pop())
                b = int(stack.pop())
                match curr:
                    case "+":
                        result = a + b
                    case "-":
                        result = b - a
                    case "*":
                        result = a * b
                    case "/":
                        result = b / a

                stack.append(result)
            else:
                stack.append(curr)

        return int(stack[-1])


