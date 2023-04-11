class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node(self):
        return self.value

class Stack:
    def __init__(self):
        self.top_node = None
        self.bottom_node = None
        self.length = 0

    def push(self, value):
        node = Node(value)

        if self.bottom_node is None:
            self.bottom_node = node
            self.top_node = self.bottom_node
            self.length = 1
            return self.bottom_node

        node.next = self.top_node
        self.top_node = node
        self.length += 1
        return self.top_node

    def pop(self):
        if self.top_node is None:
            return None

        temp = self.top_node
        self.top_node = self.top_node.next
        self.length -= 1
        return temp

    def top(self):
        return self.top_node

    def bottom(self):
        return self.bottom_node

    def len(self):
        return self.length

    def pprint(self):
        temp = self.top()

        tab = '\t'
        print(f'{tab}↸ {temp.get_node()}')
        while temp is not None:
            tab += '\t'
            temp = temp.next
            if temp is not None:
                print(f'{tab}↸ {temp.get_node()}')

# Test
stack = Stack()
stack.push('google')
stack.push('microsoft')
stack.push('facebook')
stack.pop()
stack.push('apple')

print(stack.top().value) # apple
print(stack.bottom().value) # google
print(stack.len()) # 3
stack.pprint()
# ↸ apple
# 	↸ microsoft
# 		↸ google
