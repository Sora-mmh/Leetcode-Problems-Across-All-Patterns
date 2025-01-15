from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Gauss shoelace formula
        max_area = 0
        n = len(points)
        for idx1 in range(n):
            x1, y1 = points[idx1]
            for idx2 in range(idx1 + 1, n):
                x2, y2 = points[idx2]
                for idx3 in range(idx2 + 1, n):
                    x3, y3 = points[idx3]
                    curr_area = abs(.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    max_area = max(max_area, curr_area)
        return max_area
