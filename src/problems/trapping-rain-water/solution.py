from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        height_len = len(height)

        for k in range(height_len):
            max_left = 0
            max_right = 0

            left_p = k
            right_p = k

            while left_p >= 0:
                max_left = max(max_left, height[left_p])
                left_p -= 1

            while right_p < height_len:
                max_right = max(max_right, height[right_p])
                right_p += 1

            ch = min(max_left, max_right) - height[k]

            if ch >= 0:
                total += ch

        return total

input_1 = [4,2,0,3,2,5]
print(Solution().trap(input_1))
