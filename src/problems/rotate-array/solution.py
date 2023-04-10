import time
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Original array is: [1, 2, 3, 4, 5, 6, 7]

        # step 1: reverse: [7, 6, 5, 4, 3, 2, 1]
        k %= len(nums)
        nums.reverse()

        # step 2: reverse k (k=3) itens: [5, 6, 7, ...]
        nums[:k] = nums[:k][::-1]

        # step 3: reverse k (k=3) itens: [..., 1, 2, 3, 4]
        nums[k:] = nums[k:][::-1]


# Tests
samples = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1 , -100, 3, 99],
    [1, 2]
]

s = Solution()
for key, sample in enumerate(samples, 1):
    start = time.time()
    s.rotate(sample, k=3)
    print(f'Test {key}: Tempo de execução: {time.time() - start}')
    print(f'Result: {sample}\n')
