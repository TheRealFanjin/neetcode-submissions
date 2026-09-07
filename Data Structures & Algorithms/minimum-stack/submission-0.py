class MinStack:

    def __init__(self):
        self.array = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        del self.array[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
