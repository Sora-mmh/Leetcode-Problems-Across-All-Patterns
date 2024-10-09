class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [0] * n
            dp[0], dp[1], dp[2] = 1, 2, 5
            for idx in range(3, n):
                dp[idx] = dp[idx - 3] + (dp[idx - 1] * 2)       
            return dp[-1] % (10 ** 9 + 7)
