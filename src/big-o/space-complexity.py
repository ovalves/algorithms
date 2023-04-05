# Space complexity O(1)
def boooo(n):
    for _ in range(n):
        print('booooo')

boooo(10)

# Space complexity O(n)
def array_of_hi_n_times(n):

    # pythonic way of doing array_of_hi_n_times
    # print(['hi' for _ in range(n)])

    hi_array = []
    for _ in range(n):
        hi_array.append('hi')

    print(hi_array)

array_of_hi_n_times(10)