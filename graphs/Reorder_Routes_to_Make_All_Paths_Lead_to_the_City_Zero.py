from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(dict)        
        for connection in connections:
            graph[connection[0]][connection[1]] = 1
            graph[connection[1]][connection[0]] = 0
        # edge_list = [ [] for _ in range(n)]
        # for connection in connections:
        #     edge_list[connection[0]].append(connection[1])
        queue = [0]
        edges = 0
        visited = [True] + [False] * (n - 1)
        while queue:
            curr = queue.pop()
            for node, conn in graph[curr].items():
                if not visited[node]:
                    edges += conn
                    queue.append(node)    
                    visited[node] = True
        return edges


        
