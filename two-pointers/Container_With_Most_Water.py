from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            value = min(height[left], height[right]) * (right - left)
            if value > area:
                area = value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
