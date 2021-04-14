"""
    Listas são uma sequência de valores que podem ser modificados em tempo de execução.
"""
def main():
    #
    # "a" is a string at index 0 and
    #
    """
        Lista de palavras onde:
            "A" é uma string no índice 0 e
            "E" é uma string no índice 4
    """
    letters = ["a", "b", "c", "d", "e"]
    print(letters)
    assert letters[0] == "a"
    assert letters[4] == letters[-1] == "e"

    """
        Criando uma lista dinamicamente com a função range
    """
    lista = list(range(10))

    # Exibindo os métodos disponiveis do object list
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

if __name__ == "__main__":
    main()