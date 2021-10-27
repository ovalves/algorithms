Sort Colors
====

> Site [LeetCode](https://leetcode.com/problems/sort-colors/)

> Level Medium

## Description

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
```bash
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Example 2:
```bash
Input: nums = [2,0,1]
Output: [0,1,2]
```

Example 3:
```bash
Input: nums = [0]
Output: [0]
```

Example 4:
```bash
Input: nums = [1]
Output: [1]
```

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is 0, 1, or 2.

## Solution
> Language: PHP

```php
class Solution
{

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    public function sortColors(&$nums)
    {
        $len = count($nums);

        if ($len <= 1) {
            return $nums;
        }

        for ($left = 0; $left < $len; $left++) {
            for ($right = 0; $right < $len; $right++) {
                if ($nums[$right] <= $nums[$left]) {
                    continue;
                }

                list($nums[$left], $nums[$right]) = [$nums[$right], $nums[$left]];
            }
        }

        return $nums;
    }
}
```