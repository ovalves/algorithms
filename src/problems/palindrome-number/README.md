Palindrome Number
====

> Site [LeetCode](https://leetcode.com/problems/palindrome-number/)

> Level Easy

## Description

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:
```bash
Input: x = 121
Output: true
```

Example 2:
```bash
Input: x = -121
Output: false

Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:
```bash
Input: x = 10
Output: false

Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

Example 4:
```bash
Input: x = -101
Output: false
```

Constraints:

- -231 <= x <= 231 - 1

## Solution
> Language: Python

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
```