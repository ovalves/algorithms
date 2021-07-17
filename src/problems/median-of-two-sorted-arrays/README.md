Median of Two Sorted Arrays
====

> Site [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

> Level Hard

## Description

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
```bash
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

Example 2:
```bash
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

Example 3:
```bash
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

Example 4:
```bash
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

Example 5:
```bash
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

Constraints:

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- 106 <= nums1[i], nums2[i] <= 106

## Solution
> Language: PHP

```php
<?php

class Solution
{
    /**
     * @param  int[] $nums1
     * @param  int[] $nums2
     * @return float
     */
    public function findMedianSortedArrays(array $nums1, array $nums2)
    {
        $merged = array_merge($nums1, $nums2);
        sort($merged);

        $len = count($merged);
        $median = $len / 2;

        if (0 == $len % 2) {
            return ($merged[$median] + $merged[$median - 1]) / 2;
        }

        return floor($merged[$median]);
    }
}
```