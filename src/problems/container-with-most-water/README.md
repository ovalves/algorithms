Container With Most Water
====

> Site [LeetCode](https://leetcode.com/problems/container-with-most-water)

> Level Medium

## Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the `x-axis` form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:

![Example 1](../../../assets/question_11.jpg)

```bash
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].

In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:
```bash
Input: height = [1,1]
Output: 1
```

Constraints:

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104


## Solution
> Language: Python

[Two-pointer technique](https://leetcode.com/articles/two-pointer-technique)

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_a = 0
        pointer_b = len(height) - 1
        max_area = 0

        while pointer_a < pointer_b:
            _height = min(height[pointer_a], height[pointer_b])
            _width = pointer_b - pointer_a
            _area = _height * _width
            max_area = max(max_area, _area)

            if height[pointer_a] < height[pointer_b]:
                pointer_a += 1
                continue

            pointer_b -= 1

        return max_area
```