# TODO:
# Let's do this brute force method
# Mini is not being wiped whenever the stack is updated
class MinStack:
    def __init__(self):
        # Initialize the stack that is going to persist among all function calls
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini = float('inf')
        for val in self.stack:
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini = float('inf')
            for val in self.stack:
                if val < self.mini:
                    self.mini = val

        print(self.stack)
            

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        return self.mini

        
