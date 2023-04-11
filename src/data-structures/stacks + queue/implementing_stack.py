class Stack:
    def __init__(self):
        self.matrix = []
        self.matrix_position = -1

    def push(self, value):
        self.matrix_position += 1
        self.matrix.insert(self.matrix_position, value)

    def pop(self):
        del self.matrix[self.matrix_position]
        self.matrix_position -= 1

    def top(self):
        return self.matrix[self.matrix_position]

    def bottom(self):
        return self.matrix[0]

    def len(self):
        return self.matrix_position + 1

    def pprint(self):
        if not self.matrix:
            print([])

        tab = ''
        for item in reversed(self.matrix):
            tab += '\t'
            print(f'{tab}↸ {item}')

# Test
stack = Stack()
stack.push('google')
stack.push('microsoft')
stack.push('facebook')
stack.pop()
stack.push('apple')

print(stack.top()) # apple
print(stack.bottom()) # google
print(stack.len()) # 3
stack.pprint()
# ↸ apple
# 	↸ microsoft
# 		↸ google
