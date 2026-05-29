# TODO:
# Let's do this brute force method
# Mini is not being wiped whenever the stack is updated
# Have an aux stack that is like a soft hashmap that stores the Mini at current head
class MinStack:
    def __init__(self):
        # Initialize the stack that is going to persist among all function calls
        self.stack = []
        self.aux = []
        self.mini = float('inf')
    def push(self, val: int) -> None:
        # If stack is empty
        if not self.stack:
            self.mini = val
        self.stack.append(val)
        if val < self.mini:
            self.mini = val
        self.aux.append((self.stack[-1], self.mini))
        # for val in self.stack:
        #     if val < self.mini:
        #         self.mini = val
        # 1, 1 | 2, 1 |  0, 0 
        # print(f'push {val} stack {self.stack} aux {self.aux}')

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.aux.pop()
            if self.aux:
                self.mini = self.aux[-1][1]

            # self.mini = float('inf')
            # for val in self.stack:
            #     if val < self.mini:
            #         self.mini = val

        # print(f'pop stack {self.stack} aux {self.aux}')
            

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        return self.aux[-1][1]

        
