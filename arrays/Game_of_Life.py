from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_neighbors(loc, matrix):
            m, n = len(matrix), len(matrix[0])
            i, j = loc
            movs = [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]
            neighbors = []
            for mov in movs:
                if 0 <= mov[0] < m and 0 <= mov[1] < n:
                    neighbors.append(matrix[mov[0]][mov[1]])
            return neighbors

        m, n = len(board), len(board[0])
        new_board = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                neighbors = get_neighbors((i, j), board)
                s = sum(neighbors)
                if board[i][j] == 1 and s < 2:
                    new_board[i][j] = 0
                elif board[i][j] == 1 and s in [2, 3]:
                    new_board[i][j] = 1
                elif board[i][j] == 1 and s > 3:
                    new_board[i][j] = 0
                elif board[i][j] == 0 and s == 3:
                    new_board[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]
