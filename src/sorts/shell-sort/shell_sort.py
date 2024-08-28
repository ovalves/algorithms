def shell_sort(lista):
    sort_interval = len(lista) // 2

    while sort_interval > 0:
        for i in range(sort_interval, len(lista)):
            temp = lista[i]
            j = i
            while j >= sort_interval and lista[j - sort_interval] > temp:
                lista[j] = lista[j - sort_interval]
                j -= sort_interval
            lista[j] = temp
        sort_interval //= 2

    return lista

numbers = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
print(f"Sorted: {shell_sort(numbers)}")