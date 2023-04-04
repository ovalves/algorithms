import time

"""
O(1) - Constant Time

O número de operações não depende do tamanho do array e será sempre constante.
"""
def finding_nemo(array: list) -> None:
    start = time.time()

    print(array[0]) # O(1) operation
    print(array[1]) # O(1) operation

    print(f'Tempo de execução: {time.time() - start}')

finding_nemo(['nemo'] * 10)
finding_nemo(['nemo'] * 100)
finding_nemo(['nemo'] * 100000)