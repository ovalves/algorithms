import time

"""
n represents number_list
m represents alphabet_list

O tempo de execução da função pairs é: O(n * m + m * n + m * n * 1) = O(3 * m * n)

Portanto, O(m * n * 3) = O(m * n)
"""
def pairs(alphabet_list, number_list):
    start = time.time()
    for i in range(len(alphabet_list)): # n * O(m)
        for j in range(len(number_list)): # m * O(n)
            print(alphabet_list[i],number_list[j]) # m * n * O(1)


    print(f'Tempo de execução: {time.time() - start}')

pairs(
    ['a','b','c','d','e'],
    [1,2,3,4,5]
)

