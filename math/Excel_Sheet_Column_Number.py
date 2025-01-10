class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        tot = 0
        for idx, c in enumerate(reversed(columnTitle)):
            tot += (ord(c) - ord('A') + 1) * (26 ** idx)
        return tot
