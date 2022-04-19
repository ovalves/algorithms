Two Sum
====

> Site [LeetCode](https://leetcode.com/problems/two-sum/)

> Level Easy

## Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
```bash
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:
```bash
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:
```bash
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

## Solution
> Language: PHP

```php
class Solution
{

    /**
     * @param array $nums
     * @param int $target
     * @return array
     */
    public function twoSum(array $nums, int $target): array
    {
        $len = count($nums);
        if (count($nums) <= 2) {
            return array_keys($nums);
        }

        for ($i=0; $i < $len; $i++) {
            for ($j=$i + 1; $j < $len; $j++) {
                if (($nums[$i] + $nums[$j]) == $target) {
                    return [$i, $j];
                }
            }
        }
    }
}
```