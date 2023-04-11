class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node(self) -> any:
        return self.value

class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)

        if self.first_node is None:
            self.first_node = node
            self.last_node = self.first_node
            self.length += 1
            return None

        self.last_node.next = node
        self.last_node = node
        self.length += 1

    def dequeue(self):
        if self.first_node is None:
            return None

        temp = self.first_node.next

        if temp is None:
            self.first_node = None
            self.length -= 1
            return None

        self.first_node.next = None
        self.first_node = temp
        self.length -= 1

    def first(self):
        return self.first_node

    def last(self):
        return self.last_node

    def len(self):
        return self.length

    def pprint(self):
        temp = self.first()

        tab = '\t'
        print(f'{tab}↸ {temp.get_node()}')
        while temp is not None:
            tab += '\t'
            temp = temp.next
            if temp is not None:
                print(f'{tab}↸ {temp.get_node()}')

# Test
stack = Queue()
stack.enqueue('google')
stack.enqueue('microsoft')
stack.enqueue('facebook')
stack.dequeue()
stack.enqueue('apple')

print(stack.first().value) # microsoft
print(stack.last().value) # apple
print(stack.len()) # 3
stack.pprint()
# ↸ microsoft
# 		↸ facebook
# 			↸ apple
