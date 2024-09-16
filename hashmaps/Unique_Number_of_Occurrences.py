from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        occurences = Counter(arr)
        return (
            True
            if len(set(list(occurences.values()))) == len(list(occurences.keys()))
            else False
        )
