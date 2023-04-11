import time
from typing import List

class Solution:
    def first_recurring_character(self, nums: List[int]) -> None:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = 1
                continue

            return i


# Tests
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined
samples = [
    [2,5,1,2,3,5,1,2,4],
    [2,1,1,2,3,5,1,2,4],
    [2,3,4,5],
    [3,2,3,4,5],
    [2,5,5,2,3,5,1,2,4]
]

s = Solution()

for key, sample in enumerate(samples, 1):
    start = time.time()
    res = s.first_recurring_character(sample)
    print(f'Test {key}: Tempo de execução: {time.time() - start}')
    print(f'Result: {res}\n')