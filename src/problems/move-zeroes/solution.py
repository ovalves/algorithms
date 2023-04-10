import time
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        items = 0
        for n in nums:
            if n == 0:
                items += 1

        _ = [nums.remove(0) for _ in range(items)]
        _ = [nums.append(0) for _ in range(items)]


# Tests
samples = [
    [0,0,1,0,3,0,12],
    [0],
    [0] + list(range(1000000)) + [0, 2, 4, 6, 0, 1, 3, 0] + list(range(1000000)) + [0, 2, 4, 6, 0, 1, 3, 0],
    [0,0,1],
    [0,1,0,3,12]
]

s = Solution()

for key, sample in enumerate(samples, 1):
    start = time.time()
    s.moveZeroes(sample)
    print(f'Test {key}: Tempo de execução: {time.time() - start}')
    print(f'Result: {sample}\n')
