from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key = lambda x : x[0])
        num_arrows = 1
        prev_end = sorted_points[0][1]
        for idx in range(1, len(sorted_points)):
            curr_start, curr_end = sorted_points[idx]
            if curr_start > prev_end:
                num_arrows += 1
                prev_end = curr_end
            else:
                prev_end = min(prev_end, curr_end)
        return num_arrows

            
