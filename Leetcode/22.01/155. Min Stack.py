class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        now_min = self.getMin()
        
        if now_min == None or val < now_min:
            now_min = val
        self.stack.append((val, now_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()