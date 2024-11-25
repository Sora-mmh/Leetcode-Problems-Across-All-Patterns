from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for num in range(1, n+1):
            if num % 2 == 0:
                if math.log(num) % math.log(2) == 0:
                    ans.append(1)
                else:
                    ans.append(ans[num // 2])
            else:
                ans.append(ans[-1] + 1)
        return ans
