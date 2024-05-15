Trapping Rain Water
====

> Site [LeetCode](https://leetcode.com/problems/trapping-rain-water)

> Level Hard

## Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.


Example 1:

![Example 1](../../../assets/rainwatertrap.png)

```bash
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

```

Example 2:
```bash
Input: height = [4,2,0,3,2,5]
Output: 9
```

Constraints:

- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105



## Solution
> Language: Python

[Two-pointer technique](https://leetcode.com/articles/two-pointer-technique)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        max_left = 0
        max_right = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total += max_left - height[left]

                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total += max_right - height[right]

                right -= 1

        return total
```