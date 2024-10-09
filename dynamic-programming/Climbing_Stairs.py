class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            iterator = [n] * (n + 1)
            iterator[0] = 0
            iterator[1] = 1
            iterator[2] = 2
            for a in range(n + 1):
                if a > 2:
                    iterator[a] = iterator[a - 1] + iterator[a - 2]
            return iterator[n]
