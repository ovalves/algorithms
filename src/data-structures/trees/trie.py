class Node:
    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str):
        current = self.root

        for char in word:
            if char not in current.nodes:
                current.nodes[char] = Node()
            current = current.nodes[char]

    def find(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.nodes:
                return False
            current = current.nodes[char]


trie = Trie()
trie.insert('ola')
trie.insert('mundo')
trie.insert('isso')
trie.insert('é')
trie.insert('um')
trie.insert('teste')
print(trie.find('teste')) # True