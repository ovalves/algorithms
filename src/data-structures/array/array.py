"""
    Arrays são uma sequência de valores que podem ser modificados em tempo de execução.
"""
def main():
    """
       "a" é uma string no índice 0 e
       "e" é uma string no índice 4
    """
    letters = ["a", "b", "c", "d", "e"]
    print(letters)
    assert letters[0] == "a"
    assert letters[4] == letters[-1] == "e"

    """
        Criando uma lista dinamicamente com a função range
    """
    lista = list(range(10))

    print(dir(lista))
    assert lista == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
        Checando se o número 7 está presente na lista
    """
    assert 7 in lista

    """
        Iterando pelos valores da lista
    """
    for n in lista:
        print(n)

    """
    lookup: O(1) => Pega um item usando os índices da lista
    """
    print(letters[0])

    """
    push: O(1) => Adiciona o item ao final da lista
    """
    letters.append('f')
    print(letters[-1])

    """
    unshift or insert: O(n) => Insere o item no índice informado, ajusta os índices dos demais itens do array
    """
    letters.insert(2, 'INSERTED')
    print(letters[2])

    """
    pop or delete: Remove o item no índice informado, ajusta os índices dos demais itens do array
    """
    letters.pop() # O(1)
    letters.pop(2) # O(n)
    print(letters)

if __name__ == "__main__":
    main()