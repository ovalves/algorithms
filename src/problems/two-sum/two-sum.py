class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len <= 2:
            return [0, 1]

        for k, _ in enumerate(nums):
            for j in range(k + 1, nums_len):
                if nums[k] + nums[j] == target:
                    return [k, j]