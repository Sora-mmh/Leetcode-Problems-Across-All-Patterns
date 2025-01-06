class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for num1 in range(2, int(n ** .5) + 1):
            if dp[num1]:
                dp[num1 * num1: n: num1] = [False] * ( 1 + (n - 1 - num1 * num1) // num1)
        return sum(dp)

