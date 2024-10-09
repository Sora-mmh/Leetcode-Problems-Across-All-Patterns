from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * numRow for numRow in range(1, numRows + 1)]
        if numRows >= 2:
            for idx in range(2, numRows):
                for sub_idx in range(1, idx):
                    triangle[idx][sub_idx] = (
                        triangle[idx - 1][sub_idx - 1] + triangle[idx - 1][sub_idx]
                    )
        return triangle
