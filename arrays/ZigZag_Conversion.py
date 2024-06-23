class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = 2 * numRows - 3
        jumps = [x] * numRows
        for idx in range(1, len(jumps) - 1):
            jumps[idx] = jumps[idx - 1] - 2
        result = ""
        print(jumps)
        for idx in range(numRows):
            row = []
            for s_idx in range(idx, len(s), jumps[idx] + 1):
                row.append(s[s_idx])
                print(
                    f"extracted caracters for row{idx} with jump {jumps[idx]} = {row}"
                )
                if idx != 0 and idx != numRows - 1 and len(jumps) > 3 and s_idx != idx:
                    row.append(s[s_idx + jumps[len(jumps) - 1 - idx]])
            result += "".join(row)
        return result

        # for idx in range(numRows):
        #     if idx == numRows - 1 or idx == 0:
        #         jump = x
        #     else:
        #         jump -= 2
        #     print(f"the jump for row{idx} is : {jump}")
        #     row = [s[i] for i in range(idx, len(s), jump+1)]
        #     print(f"the extracted caracters for row{idx} is : {row}")
        #     result += "".join([s[i] for i in range(idx, len(s), jump+1)])
