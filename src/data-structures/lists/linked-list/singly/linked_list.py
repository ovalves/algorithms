"""
    Faz a representação de um elemento na lista ligada.

    Cada elemento (aqui chamado de nó) terá seu valor representado como inteiro e um apontamento para o próximo elemento da lista.

    Keyword arguments:
    value -- valor do elemento
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def printNode(self):
        print(self.value)


"""
    Faz a representação da lista ligada.
"""
class LinkedList:
    def __init__(self):
        self.firstNode = None

    """
        Insere o elemento no início da lista.

        Cria um novo nó para inserção na lista
        Faz o apontamento do atributo next da classe recém criada para o valor do primeiro nó da lista ligada
        Altera o valor do primeiro nó da lista ligada com o valor do nó recém criado

        Keyword arguments:
        value -- valor do elemento a ser inserido na lista
    """
    def insertBeginning(self, value):
        node = Node(value)
        node.next = self.firstNode
        self.firstNode = node

    """
        Faz a exibição do valor do nó corrente.
    """
    def show(self):
        if self.firstNode == None:
            print('A lista está vazia')
            return None

        currentNode = self.firstNode
        while currentNode != None:
            currentNode.printNode()
            currentNode = currentNode.next

    """
        Faz a busca de um elemento lista.

        Keyword arguments:
        value -- valor do elemento a ser buscado na lista
    """
    def search(self, value):
        if self.firstNode == None:
            print('A lista está vazia')
            return None

        currentNode = self.firstNode
        while currentNode.value != value:
            if currentNode.next == None:
                return None

            currentNode = currentNode.next
        return currentNode

    """
        Deleta um elemento do começo da lista.
        Guarda o valor do primeiro nó em uma váriavel temporária (apenas para exibição do elemento excluído)

        Altera o apontamento do primeiro nó da lista para o seu sucessor
    """
    def deleteBeginning(self):
        if self.firstNode == None:
            print('A lista está vazia')
            return None

        temp = self.firstNode
        self.firstNode = self.firstNode.next
        return temp


    """
        Deleta um elemento da lista de acordo com seu valor.
        Para excluir um elemento de uma lista ligada, primeiro precisamos encontrar o elemento. Desta forma iremos percerror todos os elementos da lista até encontrarmos o elemento desejado

        Keyword arguments:
        value -- valor a ser excluído da lista
    """
    def deleteAtPosition(self, value):
        if self.firstNode == None:
            print('A lista está vazia')
            return None

        currentNode = self.firstNode
        previousNode = self.firstNode

        while currentNode.value != value:
            if currentNode.next == None:
                return None

            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode == self.firstNode:
            self.firstNode = self.firstNode.next
        else:
            previousNode.next = currentNode.next

        return currentNode

# Testes
linkedList = LinkedList()
linkedList.insertBeginning(1)
linkedList.insertBeginning(2)
linkedList.insertBeginning(3)
linkedList.insertBeginning(4)
linkedList.insertBeginning(5)
linkedList.show()

# print("---------")
# pesquisa = linkedList.search(3)
# pesquisa.printNode()

print("---------")
linkedList.deleteBeginning()
linkedList.show()
linkedList.deleteAtPosition(3)
