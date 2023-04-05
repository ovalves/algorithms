import time

"""
O tempo de execução da função find_nemo é: O(1 + m + m * 1 + k1 * 1 + 1 + 1 + 1 + n + n * 1 + k2 * 1 + 1 + 1)

Portanto, O(m + n + 2) = O(m + n)
"""
def find_nemo(first_list, second_list):
    start = time.time()

    for item in first_list: # O(m)
        if item == 'nemo': # m * O(1)
            print("Found Nemo!!")

    print(f'Tempo de execução: {time.time() - start}')

    start = time.time()
    for item in second_list: # O(m)
        if item == 'nemo': # m * O(1)
            print("Found Nemo!!")

    print(f'Tempo de execução: {time.time() - start}')

find_nemo(
    ['nemo'] * 100000,
    ['nemo'] * 100000
)