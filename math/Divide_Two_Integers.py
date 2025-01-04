class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0 and divisor < 0) or  (dividend < 0 and divisor > 0)  else 1
        if abs(dividend) < abs(divisor):
            return 0
        elif abs(dividend) == abs(divisor):
            return sign * 1
        else:
            out = sign * len(range(0, abs(dividend)-abs(divisor)+1, abs(divisor)))
            return min(max(out, -2**31), 2**31 - 1)
        

