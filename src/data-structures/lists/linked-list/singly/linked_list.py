class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_node(self):
        print(self.value)


class LinkedList:
    def __init__(self):
        self.first_node = None

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.first_node
        self.first_node = node

    def show(self):
        if self.first_node is None:
            return None

        current_node = self.first_node
        while current_node is not None:
            current_node.print_node()
            current_node = current_node.next

    def search(self, value):
        if self.first_node is None:
            print('A lista está vazia')
            return None

        current_node = self.first_node
        while current_node.value != value:
            if current_node.next is None:
                return None

            current_node = current_node.next
        return current_node

    def delete_beginning(self):
        if self.first_node is None:
            print('A lista está vazia')
            return None

        temp = self.first_node
        self.first_node = self.first_node.next
        return temp


    def delete_at_position(self, value):
        if self.first_node is None:
            print('A lista está vazia')
            return None

        current_node = self.first_node
        previous_node = self.first_node

        while current_node.value != value:
            if current_node.next is None:
                return None

            previous_node = current_node
            current_node = current_node.next

        if current_node == self.first_node:
            self.first_node = self.first_node.next
        else:
            previous_node.next = current_node.next

        return current_node

# Test
linkedList = LinkedList()
linkedList.insert_beginning(1)
linkedList.insert_beginning(2)
linkedList.insert_beginning(3)
linkedList.insert_beginning(4)
linkedList.insert_beginning(5)
linkedList.show()

# print("---------")
# pesquisa = linkedList.search(3)
# pesquisa.print_node()

print("---------")
linkedList.delete_beginning()
linkedList.show()
linkedList.delete_at_position(3)
