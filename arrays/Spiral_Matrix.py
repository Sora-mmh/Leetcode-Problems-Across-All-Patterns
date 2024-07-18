from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import numpy as np

        values = []

        def spiralOneOrder(matrix):
            x, y = matrix.shape
            if x != 0 and y != 0:
                first_row = matrix[0, :]
                values.extend(first_row)
                if x > 1:
                    last_column = matrix[1:-1, -1]
                    last_row = matrix[-1, :][::-1]
                    values.extend(last_column)
                    values.extend(last_row)
                if y > 1:
                    first_column = matrix[1:-1, 0][::-1]
                    values.extend(first_column)
                spiralOneOrder(matrix[1:-1, 1:-1])

        spiralOneOrder(np.array(matrix))
        return values
