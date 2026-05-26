class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # This dictionary reduces mental overhead when matching up valid closing and opening brackets
        hashy = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for curr in s:
            if curr in '{([':
                stack.append(curr)
            else:
            # In here we are comparing closing brackets
                if not stack:
                    return False

                top = stack.pop()
                if top != hashy[curr]:
                    return False
        return not stack
