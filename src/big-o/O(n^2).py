import time

"""
O tempo de execução da função log_all_pairs é: O(n * n + n * n + n * n * 1) = O(3n^2)

Portanto, O(3n^2) = O(n^2)
"""
def log_all_pairs(array):
    start = time.time()
    for first in range(len(array)): # n * O(n)
        for second in range(len(array)): # n * O(n)
            print(array[first], array[second]) # n * n * O(1)

    print(f'Tempo de execução: {time.time() - start}')

log_all_pairs(['a','b','c','d','e'])