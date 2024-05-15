from typing import List

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

input_1 = [4,2,0,3,2,5]
print(Solution().trap(input_1))
