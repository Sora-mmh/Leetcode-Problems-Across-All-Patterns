from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        digits_str = "123456789"

        def check_entire_row(row_list: List[int]):
            digits_occ = {e:0 for e in row_list}
            for e in row_list:
                if e in digits_str:
                    digits_occ[e] += 1 
            return all([e in [0, 1] for e in list(digits_occ.values())])

        def check_entire_column(col_list: List[int]):
            digits_occ = {e:0 for e in col_list}
            for e in col_list:
                if e in digits_str:
                    digits_occ[e] += 1 
            return all([e in [0, 1] for e in list(digits_occ.values())])


        def check_three_by_three(min_board):
            digits_occ = {}
            for row in range(3):
                for col in range(3):
                    digits_occ[min_board[row, col]] = 0
            for row in range(3):
                for col in range(3):
                    if min_board[row, col] in digits_str:
                        digits_occ[min_board[row, col]] += 1
            return all([e in [0, 1] for e in list(digits_occ.values())])

        board = np.array(board)

        for row in range(9):
            if not check_entire_row(board[row, :]):
                return False

        for col in range(9):
            if not check_entire_column(board[:, col]):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not check_three_by_three(board[row: row + 3, col : col + 3]):
                    return False
                
        return True

