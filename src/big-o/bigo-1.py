#!/usr/local/bin/python3
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

def soma2(n):
    return (n * (n + 1)) / 2

if __name__ == '__main__':
    # Tool for measuring execution time of small code snippets.
    import timeit

    # Checagem de tempo de execução da primeira função de soma
    t1 = timeit.Timer("soma1(100_000)", "from __main__ import soma1")
    print(f"soma1 ran: {t1.timeit(number=1000)} milliseconds | final value: {soma1(100_000)}")

    # Checagem de tempo de execução da segunda função de soma
    t1 = timeit.Timer("soma2(100_000)", "from __main__ import soma2")
    print(f"soma2 ran: {t1.timeit(number=1000)} milliseconds | final value: {soma2(100_000)}")