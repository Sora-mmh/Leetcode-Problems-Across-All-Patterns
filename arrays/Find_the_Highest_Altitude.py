from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for idx in range(len(gain)):
            altitudes.append(gain[idx] + altitudes[-1])
        return max(altitudes)
