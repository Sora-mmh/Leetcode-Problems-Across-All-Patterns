    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        nd =  n // 2
        st = n - nd
        res = pow(5, st, m) * pow(4, nd, m)
        return res % m
