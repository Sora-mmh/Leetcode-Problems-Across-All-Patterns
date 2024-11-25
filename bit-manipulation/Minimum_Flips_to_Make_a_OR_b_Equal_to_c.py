class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while c or a or b:
            a_ = a & 1
            b_ = b & 1
            c_ = c & 1
            if c_ != (a_ or b_):
                ans += 1
                if not c_ and (a_ and b_):
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
