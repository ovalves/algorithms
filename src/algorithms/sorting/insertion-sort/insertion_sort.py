def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        index_marked = lista[i]

        j = i - 1
        while j >= 0 and index_marked < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = index_marked

    return lista

insertion_sort([12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7])