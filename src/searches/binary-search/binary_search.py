from typing import List

def binary_search(numbers: List[int], target: int):
    lower_limit = 0
    upper_limit = len(numbers) - 1

    while lower_limit <= upper_limit:
        middle = int((lower_limit + upper_limit) / 2)
        if numbers[middle] == target:
            return middle

        if numbers[middle] > target:
            upper_limit = middle - 1
        else:
            lower_limit = middle + 1
    return None  # None => Número não encontrado na lista


numbers = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
print(f"Número de iterações: {binary_search(numbers, 7)}")
print(f"Número de iterações: {binary_search(numbers, 13)}")
