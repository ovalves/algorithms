from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_a = 0
        pointer_b = len(height) - 1
        max_area = 0

        while pointer_a < pointer_b:
            _height = min(height[pointer_a], height[pointer_b])
            _width = pointer_b - pointer_a
            _area = _height * _width
            max_area = max(max_area, _area)

            if height[pointer_a] < height[pointer_b]:
                pointer_a += 1
                continue

            pointer_b -= 1

        return max_area


input1 = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(input1))
