#!/usr/local/bin/python3
def lista1():
    lista = []
    for i in range(100_000):
        lista += [i]
    return lista

def lista2():
    return range(0, 100_000)

if __name__ == '__main__':
    # Tool for measuring execution time of small code snippets.
    import timeit

    # Checagem de tempo de execução da primeira função de lista
    t1 = timeit.Timer("lista1()", "from __main__ import lista1")
    print(f"lista1 ran: {t1.timeit(number=1000)} milliseconds | final value: {len(lista1())}")

    # Checagem de tempo de execução da segunda função de lista
    t1 = timeit.Timer("lista2()", "from __main__ import lista2")
    print(f"lista2 ran: {t1.timeit(number=1000)} milliseconds | final value: {len(lista2())}")