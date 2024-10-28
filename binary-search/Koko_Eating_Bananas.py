from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        min_k = end
        while start <= end:
            k = (start + end) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                min_k = k
                end = k - 1
            else:
                start = k + 1
        return min_k
            
