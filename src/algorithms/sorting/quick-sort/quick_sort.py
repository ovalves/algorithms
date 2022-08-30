def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    lower = [i for i in array[1:] if i <= pivot]
    upper = [i for i in array[1:] if i > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(upper)

numbers = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
print(f"Sorted: {quick_sort(numbers)}")