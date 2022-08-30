def merge_sort(lista):
    if len(lista) > 1:
        split = len(lista)//2
        left_vector = lista[:split].copy()
        right_vector = lista[split:].copy()

        merge_sort(left_vector)
        merge_sort(right_vector)

        i = j = k = 0

        while i < len(left_vector) and j < len(right_vector):
            if left_vector[i] < right_vector[j]:
                lista[k] = left_vector[i]
                i += 1
            else:
                lista[k] = right_vector[j]
                j += 1
            k += 1

        while i < len(left_vector):
            lista[k] = left_vector[i]
            i += 1
            k += 1

        while j < len(right_vector):
            lista[k] = right_vector[j]
            j += 1
            k += 1

    return lista

numbers = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
print(f"Sorted: {merge_sort(numbers)}")