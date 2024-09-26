class Solution:
    def isHappy(self, n: int) -> bool:
        n_list = list(str(n))
        n = sum([int(nn) ** 2 for nn in n_list])
        visited = set()
        while n not in visited:
            visited.add(n)
            n_list = list(str(n))
            n = sum([int(nn) ** 2 for nn in n_list])
            if n == 1:
                return True
        return False
