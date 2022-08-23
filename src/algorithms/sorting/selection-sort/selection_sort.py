def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        index_min_value = i
        for j in range(i + 1, n):
            if lista[index_min_value] > lista[j]:
                index_min_value = j

        temp = lista[i]
        lista[i] = lista[index_min_value]
        lista[index_min_value] = temp

    return lista

print(selection_sort([12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]))