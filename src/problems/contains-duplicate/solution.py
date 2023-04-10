import time
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Tests
samples = [
    list(range(10000000)) + [1, 2],
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
]

s = Solution()

for key, sample in enumerate(samples, 1):
    start = time.time()
    result = s.containsDuplicate(sample)
    print(f'Test {key}: Tempo de execução: {time.time() - start}')
    print(f'Result: {result}\n')
