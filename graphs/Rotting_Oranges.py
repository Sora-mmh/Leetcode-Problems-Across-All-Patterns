from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import collections
        m, n = len(grid), len(grid[0])
        queue = collections.deque([])
        positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh, minutes = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
        if fresh == 0:
            return 0
        if not queue:
            return -1
        while queue:
            for _ in range(len(queue)):
                current_pos = queue.popleft()
                for pos in positions:
                    neighbor = [current_pos[0] + pos[0], current_pos[1] + pos[1]]
                    if 0 <= neighbor[0] < m and  0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == 1:
                            grid[neighbor[0]][neighbor[1]] = 2 
                            fresh -= 1
                            queue.append(neighbor)
            minutes += 1
        return -1 if fresh != 0 else minutes - 1        
