from heapq import heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_score, s = 0, 0
        minh = []
        for num1, num2 in sorted(
            list(zip(nums1, nums2)), key=lambda item: item[1], reverse=True
        ):
            s += num1
            heappush(minh, num1)
            if len(minh) == k:
                max_score = max(max_score, s * num2)
                s -= heappop(minh)
        return max_score
