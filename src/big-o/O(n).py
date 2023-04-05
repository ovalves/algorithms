import time

"""
O(n) - Linear time
"""
def find_nemo(array: list) -> None:
    start = time.time()

    for item in array:
        if item == 'nemo':
            print("Found Nemo!!")

    print(f'Tempo de execução: {time.time() - start}')

find_nemo(['nemo'])
find_nemo(['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla'])
find_nemo(['nemo'] * 100000)