from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1] * idx for idx in range(1, rowIndex + 2)]
        if rowIndex >= 2:
            for idx in range(2, len(triangle)):
                for sub_idx in range(1, idx):
                    triangle[idx][sub_idx] = (
                        triangle[idx - 1][sub_idx - 1] + triangle[idx - 1][sub_idx]
                    )
        return triangle[-1]
