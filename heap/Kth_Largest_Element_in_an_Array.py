import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = nums[:k]
        heapq.heapify(k_largest)
        n = len(nums)
        for idx in range(k, n):
            if nums[idx] > k_largest[0]:
                heapq.heappop(k_largest)
                heapq.heappush(k_largest, nums[idx])
        return k_largest[0]
