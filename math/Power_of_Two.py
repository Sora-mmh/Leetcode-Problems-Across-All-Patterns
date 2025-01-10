class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n == 0:
            return False
        elif n < 0:
            p = math.log(-n, 2)
            return 2 ** int(p) == n
        else:
            p = math.log(n, 2)
            return 2 ** int(p) == n
        
