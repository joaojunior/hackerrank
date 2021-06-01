from typing import List


class Solution:
    def make_connected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        self.adjacents = {}
        self.visited = {}
        for i in range(n):
            self.adjacents[i] = []
            self.visited[i] = False
        for i, j in connections:
            self.adjacents[i].append(j)
            self.adjacents[j].append(i)
        components = 0
        for i in range(n):
            if self.visited[i] is False:
                self.dfs(i)
                components += 1
        return components - 1

    def dfs(self, i):
        if self.visited[i] is False:
            self.visited[i] = True
            for j in self.adjacents[i]:
                self.dfs(j)
