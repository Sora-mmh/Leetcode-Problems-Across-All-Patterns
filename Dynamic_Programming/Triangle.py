from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def minimumLevel(row, idx):
            if row >= len(triangle):
                return 0
            else:
                return triangle[row][idx] + min(
                    minimumLevel(row + 1, idx), minimumLevel(row + 1, idx + 1)
                )

        return minimumLevel(0, 0)
