Rotate Array
====

> Site [LeetCode](https://leetcode.com/problems/rotate-array)

> Level Medium

## Description

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
```bash
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

Example 2:
```bash
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

Constraints:

- 1 <= nums.length <= 1<sup>05
- -2<sup>31 <= nums[i] <= 2<sup>31 - 1
- 0 <= k <= 1<sup>05


## Solution
> Language: Python

```python
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
```