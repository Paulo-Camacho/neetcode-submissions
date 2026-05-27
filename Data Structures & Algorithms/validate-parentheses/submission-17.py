class Solution:
    def isValid(self, s: str) -> bool:
        hashy = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []

        for bracket in s:
            # Building set until we find a closing bracket
            if bracket in '({[':
                stack.append(bracket)
            else:
                # This is enough to catch a non corresponding bracket when met with a closing
                if not stack:
                    return False
                top = stack.pop()
                if top != hashy[bracket]:
                    return False
        return not stack
                


