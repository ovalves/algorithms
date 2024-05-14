from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for pointer_a, _ in enumerate(height):
            for pointer_b in range(pointer_a + 1, len(height)):
                _height = min(height[pointer_a], height[pointer_b])
                _width = pointer_b - pointer_a
                _area = _height * _width
                max_area = max(max_area, _area)

        return max_area



input1 = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(input1))
