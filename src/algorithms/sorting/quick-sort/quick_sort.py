def partition(vector, start, end):
    pivot = vector[end]
    i = start - 1

    for j in range(start, end):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i + 1], vector[end] = vector[end], vector[i + 1]
    return i + 1


def quick_sort(vector, start, end):
    if start < end:
        position = partition(vector, start, end)

        # Left Side
        quick_sort(vector, start, position - 1)

        # Right Side
        quick_sort(vector, position + 1, end)
    return vector

vector = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
quick_sort(vector, 0, len(vector) - 1)
