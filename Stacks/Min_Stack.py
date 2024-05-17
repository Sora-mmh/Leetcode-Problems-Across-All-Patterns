class MinStack:

    def __init__(self) -> None:
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return min(self.min_stack)
        # min_value = self.min_stack[0]
        # for idx in range(1, len(self.min_stack)):
        #     if self.min_stack[idx] < min_value:
        #         min_value = self.min_stack[idx]
        # return min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
