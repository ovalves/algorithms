def has_pair_with_sum(array, sum):
    arr_set = set()

    for i in array:
        if i in arr_set:
            return True

        arr_set.add(sum - i)

    return False

print(has_pair_with_sum([7, 2, 3, 1], 8))
print(has_pair_with_sum([1, 2, 3, 9], 8))
print(has_pair_with_sum([1, 2, 4, 4], 8))