class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            x = 2 * numRows - 3
            jumps = [x] * numRows
            for idx in range(1, len(jumps) - 1):
                jumps[idx] = jumps[idx - 1] - 2
            result = ""
            for row, jump in enumerate(jumps):
                idx = row
                while idx < len(s):
                    if idx < len(s):
                        result += s[idx]
                    else:
                        break
                    if row != 0 and row != numRows - 1 and numRows - 1 - row != row:
                        idx += jump + 1
                        if idx < len(s):
                            result += s[idx]
                        else:
                            break
                        idx += jumps[numRows - 1 - row] + 1
                    else:
                        idx += jump + 1
            return result
