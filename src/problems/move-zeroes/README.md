Move Zeroes
====

> Site [LeetCode](https://leetcode.com/problems/move-zeroes)

> Level Easy

## Description

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
```bash
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Example 2:
```bash
Input: nums = [0]
Output: [0]
```

Constraints:

- 1 <= nums.length <= 10<sup>4
- -2<sup>31 <= nums[i] <= 2<sup>31 - 1

## Solution
> Language: Python

```python
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
```