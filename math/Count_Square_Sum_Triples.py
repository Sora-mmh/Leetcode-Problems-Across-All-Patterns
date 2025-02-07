class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(1, n):
                sqr = sqrt(a ** 2 + b ** 2)
                if sqr == int(sqr) and sqr <= n:
                    count += 1
        return count
        
