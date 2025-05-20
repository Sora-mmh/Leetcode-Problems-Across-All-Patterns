class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        i = 1
        while i < n:
            res ^= start + 2 * i
            i += 1
        return res 
