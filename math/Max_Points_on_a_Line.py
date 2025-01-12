from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def compute_tan(p1, p2):
            if (p1[0] - p2[0]) != 0:
                return (p1[1] - p2[1]) / (p1[0] - p2[0])
            else:
                return inf
        if len(points) <= 2:
            return len(points)
        res = 1
        for idx, p1 in enumerate(points):
            tans = defaultdict(int)
            for p2 in points[idx + 1:]:
                tan = compute_tan(p1, p2)
                tans[tan] += 1
                res = max(tans[tan], res)
        return res + 1

