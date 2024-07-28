from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        pairs = []
        potions = sorted(potions)
        m = len(potions)
        import bisect

        for spell in spells:
            # Solution 1
            pairs.append(len(potions) - bisect_left(potions, success / spell))
            # Solution 2
            # potion_idx = m - 1
            # counter = 0
            # while potions[potion_idx] * spell >= success and potion_idx >= 0:
            #     potion_idx -= 1
            #     counter += 1
            # pairs.append(counter)
        return pairs
