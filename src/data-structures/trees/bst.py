from typing import Union

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Union[Node, None] = None

    def insert(self, root: Union[Node, None], value: int = None) -> Node:
        if root is None:
            return Node(value)

        if root.value == value:
            return root

        if value < root.value:
            root.left = self.insert(root.left, value)
            return root

        root.right = self.insert(root.right, value)
        return root


    def lookup(self, root: Union[Node, None], value: int) -> Union[Node, None]:
        if root is None or root.value == value:
            return root

        if value < root.value:
            return self.lookup(root.left, value)

        return self.lookup(root.right, value)


    def exists(self, root: Union[Node, None], value: int) -> bool:
        return self.lookup(root, value) is not None

    def search(self, root: Union[Node, None], value: int) -> Union[Node, None]:
        _node = self.lookup(root, value)
        return _node.value if isinstance(_node, Node) else None

    def in_order(self, root) -> None:
        if root:
            self.in_order(root.left)
            print(f'↳ {root.value}')
            self.in_order(root.right)

    def print_tree(self, root: Union[Node, None], level=0) -> None:
        if root is not None:
            self.print_tree(root.right, level + 1)
            print(' ' * 4 * level + str(root.value) + ' ↢ ')
            self.print_tree(root.left, level + 1)


tree = BinarySearchTree()
node = Node(9)
node = tree.insert(node, 4)
node = tree.insert(node, 6)
node = tree.insert(node, 20)
node = tree.insert(node, 170)
node = tree.insert(node, 15)
node = tree.insert(node, 1)
print(tree.exists(node, 20)) # True
print(tree.search(node, 3)) # None
print(tree.search(node, 170)) # 170
tree.in_order(node)
# ↳ 1
# ↳ 4
# ↳ 6
# ↳ 9
# ↳ 15
# ↳ 20
# ↳ 170

tree.print_tree(node)
#         170↢
#     20↢
#         15↢
# 9↢
#         6↢
#     4↢
#         1↢
