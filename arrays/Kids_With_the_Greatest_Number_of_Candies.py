class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        results = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                results.append(True)
            else:
                results.append(False)
        return results
