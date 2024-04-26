from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        fresh_oranges_counter = len(
            [grid[i][j] for i in range(m) for j in range(n) if grid[i][j] == 1]
        )
        contamination = False
        visited = []
        if len(q) == 0:
            if m * n == (m * n - fresh_oranges_counter):
                return 0
            else:
                return -1
        minutes = 0
        while q:
            cur_ii, cur_jj = q.popleft()
            visited.append((cur_ii, cur_jj))
            neighbors = [
                (cur_ii + ii, cur_jj + jj)
                for ii, jj in [(0, -1), (-1, 0), (0, 1), (1, 0)]
                if 0 <= cur_ii + ii < m and 0 <= cur_jj + jj < n
            ]
            for ii, jj in neighbors:
                if grid[ii][jj] == 1:
                    grid[ii][jj] = 2
                    fresh_oranges_counter -= 1
                    contamination = True
                    if (ii, jj) not in visited and (ii, jj) not in q:
                        q.append((ii, jj))
            if contamination:
                minutes += 1
                contamination = False
        if fresh_oranges_counter != 0:
            return -1
        else:
            return minutes
