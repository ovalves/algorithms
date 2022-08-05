Combination Sum IV
====

> Site [LeetCode](https://leetcode.com/problems/combination-sum-iv/)

> Level Medium

## Description

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
```bash
Input: nums = [1,2,3], target = 4
Output: 7

Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

Example 2:
```bash
Input: nums = [9], target = 3
Output: 0
```

Constraints:

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000

## Solution
> Language: Go

```go
func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1

	for t := 1; t <= target; t++ {
		for _, n := range nums {
			if t >= n {
				dp[t] += dp[t-n]
			}
		}
	}
	return dp[target]
}
```