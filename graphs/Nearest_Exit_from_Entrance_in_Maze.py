from typing impory List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])    
        visited = [ [0] * n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = 1
        queue = [[entrance, 0]]
        positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            current_pos, step = queue.pop(0)
            for pos in positions:
                next_pos = [current_pos[0] + pos[0], current_pos[1] + pos[1]]
                if 0 <= next_pos[0] < m and 0 <= next_pos[1] < n and visited[next_pos[0]][next_pos[1]] == 0 and maze[next_pos[0]][next_pos[1]] == ".":
                    if (next_pos[0] in [0, m - 1] or next_pos[1] in [0, n - 1])  and not (next_pos[0] == entrance[0] and next_pos[1] == entrance[1]):
                        return step + 1
                    visited[next_pos[0]][next_pos[1]] = 1
                    queue.append([next_pos, step + 1])
        return -1
        
        
