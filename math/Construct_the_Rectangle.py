from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        max_W = int(math.sqrt(area))
        possibilities = []
        for w in range(1, max_W + 1):
            L = area // w
            if w * L == area:
                possibilities.append([L, w])
        return possibilities[-1]
        
