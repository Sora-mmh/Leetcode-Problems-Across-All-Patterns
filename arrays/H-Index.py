from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        sorted_citations = sorted(citations, reverse=True)
        idx = 0
        while idx < len(sorted_citations) and sorted_citations[idx] >= idx + 1:
            h_index += 1
            idx += 1
        return h_index
