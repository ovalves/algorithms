Reverse Integer
====

> Site [LeetCode](https://leetcode.com/problems/reverse-integer/)

> Level Easy

## Description

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
```bash
Input: x = 123
Output: 321
```

Example 2:
```bash
Input: x = -123
Output: -321
```

Example 3:
```bash
Input: x = 120
Output: 21
```

Example 4:
```bash
Input: x = 0
Output: 0
```

Constraints:

- -231 <= x <= 231 - 1

## Solution
> Language: Python

```python
class Solution:
    def reverse(self, x: int) -> int:
        if not x < 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(x)[:1] + str(x)[1:][::-1])

        if x not in range((-1 << 31), (1 << 31) - 1):
            return 0
        return x
```