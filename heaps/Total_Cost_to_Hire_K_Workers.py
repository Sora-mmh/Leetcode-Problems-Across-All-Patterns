from heapq import heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_minh = []
        right_minh = []
        cost = 0
        left_counter, right_counter = 0, len(costs) - 1
        session = 0
        while session < k:
            while len(left_minh) < candidates and left_counter <= right_counter:
                heappush(left_minh, costs[left_counter])
                left_counter += 1
            while len(right_minh) < candidates and left_counter <= right_counter:
                heappush(right_minh, costs[right_counter])
                right_counter -= 1
            left_min = left_minh[0] if left_minh else float("inf")
            right_min = right_minh[0] if right_minh else float("inf")
            if left_min <= right_min:
                cost += left_min
                heappop(left_minh)
            else:
                cost += right_min
                heappop(right_minh)
            session += 1
        return cost
