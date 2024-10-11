from typing import List
import collections

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = []
        graph = collections.defaultdict(list)
        for idx in range(len(rooms)):
            graph[idx] = rooms[idx]
        for idx in graph[0]:
            queue.append(idx)
        visited.add(0)
        while queue:
            current_room = queue.pop()
            visited.add(current_room)
            for idx in rooms[current_room]:
                if idx not in visited:
                    queue.append(idx)
        return len(visited) == len(rooms)
