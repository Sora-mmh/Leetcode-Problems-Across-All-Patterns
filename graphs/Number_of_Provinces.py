from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
      
        def check(idx):
            visited[idx] = True
            for i, connect in enumerate(isConnected[idx]):
                if connect == 1 and not visited[i]:
                    check(i)
                 
        for idx in range(n):
            if not visited[idx]:
                check(idx)
                provinces += 1
        return provinces
