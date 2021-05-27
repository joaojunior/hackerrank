from typing import List


class Solution:
    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        q = list(range(n))
        provinces = 0
        visited = {}
        for city in q:
            visited[city] = False
        q = [0]
        while not all(visited.values()):
            while q:
                city = q.pop(0)
                visited[city] = True
                for adj, presence in enumerate(is_connected[city]):
                    if visited[adj] is False and presence == 1:
                        q.append(adj)
            city = 0
            while visited.get(city, False) is True:
                city += 1
            q = [city]
            provinces += 1
        return provinces
