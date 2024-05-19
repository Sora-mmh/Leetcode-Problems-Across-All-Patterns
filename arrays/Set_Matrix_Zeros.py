from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        root_locations = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    root_locations.append((i, j))
        all_zeros_locations = []
        for zero_location in root_locations:
            i, j = zero_location
            for k in range(m):
                all_zeros_locations.append((k, j))
            for k in range(n):
                all_zeros_locations.append((i, k))
        all_zeros_locations.extend(root_locations)
        for zero_location in set(all_zeros_locations):
            i, j = zero_location
            matrix[i][j] = 0
