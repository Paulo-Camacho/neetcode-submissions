class Solution:
    def isValid(self, s: str) -> bool:
        # Keep the opening pattern, we can use a stack for that
        stack = []
        if len(s) <= 1:
            return False
        hashy = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for bracket in s:
                if bracket == '{' or bracket == '[' or bracket == '(':
                    stack.append(bracket)
                else:
                    # If we see a closing bracket and the stack is empty just return False
                    if not stack:
                        return False
                    top = stack.pop()
                    if top != hashy[bracket]:
                        return False
                
        print(stack)
        # I want it to print true if the stack is empty
        if not stack:
            return True
        else:
            return False

