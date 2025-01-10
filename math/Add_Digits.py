class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) != 1:
            tot = 0
            for c in s:
                tot += int(c)
            s = str(tot)
        return int(s)
        
