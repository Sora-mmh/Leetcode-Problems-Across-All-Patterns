from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid_wrt_rows = grid
        grid_wrt_cols = [[] for _ in range(n)]
        for col in range(n):
            for row in range(m):
                grid_wrt_cols[col].append(grid[row][col])
        pairs_counter = 0
        for row in grid_wrt_rows:
            for col in grid_wrt_cols:
                if row == col:
                    pairs_counter += 1
        return pairs_counter
