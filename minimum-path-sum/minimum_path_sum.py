import heapq
from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        return self.dijkstra(grid)

    def dijkstra(self, grid: List[List[int]]) -> int:
        inf = float("inf")
        m = len(grid)
        n = len(grid[0])
        visited = {}
        distances = {}
        for i in range(m):
            for j in range(n):
                distances[(i, j)] = inf
        distances[(0, 0)] = grid[0][0]
        q = [(grid[0][0], 0, 0)]
        while q:
            _, x, y = heapq.heappop(q)
            visited[(x, y)] = True
            if x + 1 < m and (distances[(x, y)] +
                              grid[x+1][y] < distances[(x+1, y)]):
                distances[(x+1, y)] = distances[(x, y)] + grid[x+1][y]
                if visited.get((x+1, y), False) is False:
                    visited[(x+1, y)] = True
                    heapq.heappush(q, (distances[(x+1, y)], x+1, y))
            if y + 1 < n and (distances[(x, y)] +
                              grid[x][y+1] < distances[(x, y+1)]):
                distances[(x, y+1)] = distances[(x, y)] + grid[x][y+1]
                if visited.get((x, y+1), False) is False:
                    visited[(x, y+1)] = True
                    heapq.heappush(q, (distances[(x, y+1)], x, y+1))
        return distances[(m-1, n-1)]
