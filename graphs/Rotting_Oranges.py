from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def intersect(l1: List[int], l2: List[int]) -> bool:
            if len(list(set(l1) & set(l2))) == 0:
                return False
            else:
                return True

        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        last_q = q.copy()
        visited = []
        history = []
        if len(q) == 0:
            return -1
        minutes = 0
        while q:
            # print("q", q)
            # print(visited)
            cur_ii, cur_jj = q.popleft()
            visited.append((cur_ii, cur_jj))
            neighbors = [
                (cur_ii + ii, cur_jj + jj)
                for ii, jj in [(0, -1), (-1, 0), (0, 1), (1, 0)]
                if 0 <= cur_ii + ii < m and 0 <= cur_jj + jj < n
            ]
            history.append(neighbors)
            for ii, jj in neighbors:
                if grid[ii][jj] == 1:
                    grid[ii][jj] == 2
                    if (ii, jj) not in visited and (ii, jj) not in q:
                        q.append((ii, jj))
                elif grid[ii][jj] == 2:
                    if grid[cur_ii][cur_jj] == 1:
                        grid[cur_ii][cur_jj] = 2
            print("last_q", last_q)
            print("q", q)
            if not intersect(last_q, q):
                minutes += 1
            last_q = q.copy()
        return minutes
