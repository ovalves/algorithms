def merge_sort(lista):
    if len(lista) > 1:
        split = len(lista)//2
        leftVector = lista[:split].copy()
        rightVector = lista[split:].copy()

        merge_sort(leftVector)
        merge_sort(rightVector)

        i = j = k = 0

        # Ordena leftVector e rightVector
        while i < len(leftVector) and j < len(rightVector):
            if leftVector[i] < rightVector[j]:
                lista[k] = leftVector[i]
                i += 1
            else:
                lista[k] = rightVector[j]
                j += 1
            k += 1

        # Ordenação final
        while i < len(leftVector):
            lista[k] = leftVector[i]
            i += 1
            k += 1

        while j < len(rightVector):
            lista[k] = rightVector[j]
            j += 1
            k += 1

    return lista

merge_sort([12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7])