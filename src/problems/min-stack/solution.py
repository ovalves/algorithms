class MinStack:

    def __init__(self):
        self.matrix = []
        self.matrixPosition = -1

    def push(self, val: int) -> None:
        self.matrixPosition += 1
        self.matrix.insert(self.matrixPosition, val)

    def pop(self) -> None:
        del self.matrix[self.matrixPosition]
        self.matrixPosition -= 1

    def top(self) -> int:
        return int(self.matrix[self.matrixPosition])

    def getMin(self) -> int:
        return int(min(self.matrix))


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(f'min {minStack.getMin()}\n') # return -3
minStack.pop()
print(f'top {minStack.top()}') # return 0
print(f'min {minStack.getMin()}') # return -2