from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Floyd-Warshall Algorithm
        graph = defaultdict(dict)
        for (var1, var2), val in zip(equations, values):
            graph[var1][var1] = graph[var2][var2] = 1
            graph[var1][var2] = val
            graph[var2][var1] = 1 / val
            
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j] if i != j else 1.

        return [graph[u].get(v, -1) for u,v in queries]
        
        
