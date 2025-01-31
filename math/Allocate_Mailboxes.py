class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        @cache
        def minDist(s, e, k):
            if s == e:
                return 0
            if k == 1:
                m = (e + s + 1) // 2
                d = 0
                for idx in range(s, e + 1):
                    d += abs(houses[m] - houses[idx])
                return d
            else:
                d = float('inf')
                for idx in range(s, e):
                    d = min(d, minDist(s, idx, 1) + minDist(idx + 1, e, k - 1))
                return d
        return minDist(0, n - 1, k)
