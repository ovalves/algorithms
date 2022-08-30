def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista

numbers = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
print(f"Sorted: {bubble_sort(numbers)}")