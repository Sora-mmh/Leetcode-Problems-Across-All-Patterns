from typing import List
from collections import deque


# This solution is a lot easier using a queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = m * n
        while q:
            ii, jj = q.popleft()
            for r, c in [left, right, down, up]:
                if 0 <= ii + r < m and 0 <= jj + c < n:
                    if mat[ii + r][jj + c] > mat[ii][jj] + 1:
                        q.append((ii + r, jj + c))
                        mat[ii + r][jj + c] = mat[ii][jj] + 1
        return mat


# A little bit complex : this solution gets the levels around a value and the distance is the level iteself
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def find_lvl_combinations(lvl):
            l1, l2 = [-e for e in range(-lvl, lvl + 1)], [
                -e for e in range(-lvl, lvl + 1)
            ]
            combinations = [(e1, e2) for e1 in l1 for e2 in l2 if abs(e1 + e2) == lvl]
            return combinations

        import numpy as np

        m, n = len(mat), len(mat[0])
        updated_mat = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    updated_mat.append(0)
                else:
                    lvl = 1
                    neighbors_per_lvl = find_lvl_combinations(lvl)
                    lvl_neighbors = [
                        mat[i + ii][j + jj]
                        for (ii, jj) in neighbors_per_lvl
                        if (i + ii >= 0 and i + ii < m) and (j + jj >= 0 and j + jj < n)
                    ]
                    print(lvl_neighbors)
                    if 0 in lvl_neighbors:
                        updated_mat.append(0)
                    elif len(lvl_neighbors) == 0:
                        updated_mat.append(0)
                    else:
                        lvl += 1
                        neighbors_per_lvl = find_lvl_combinations(lvl)
                        lvl_neighbors = [
                            mat[i + ii][j + jj]
                            for (ii, jj) in neighbors_per_lvl
                            if (i + ii >= 0 and i + ii < m)
                            and (j + jj >= 0 and j + jj < n)
                        ]
                        while 0 not in lvl_neighbors:
                            lvl += 1
                            neighbors_per_lvl = find_lvl_combinations(lvl)
                            lvl_neighbors = [
                                mat[i + ii][j + jj]
                                for (ii, jj) in neighbors_per_lvl
                                if (i + ii >= 0 and i + ii < m)
                                and (j + jj >= 0 and j + jj < n)
                            ]
                        if len(lvl_neighbors) == 0:
                            updated_mat.append(0)
                        if 0 in lvl_neighbors:
                            updated_mat.append(lvl)
        return np.array(updated_mat).reshape((m, n))
