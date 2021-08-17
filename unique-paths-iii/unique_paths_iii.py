from typing import List


class Solution:
    def unique_paths_III(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = {}
        self.grid = grid
        start_i = 0
        start_j = 0
        self.obstacles = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                    self.visited[(i, j)] = True
                elif grid[i][j] == -1:
                    self.obstacles += 1
        return self.dfs(start_i, start_j, 1)

    def dfs(self, i: int, j: int, visiteds: int) -> int:
        if (self.grid[i][j] == 2 and
                visiteds == self.m * self.n - self.obstacles):
            return 1
        elif self.grid[i][j] == -1:
            return 0
        else:
            result = 0
            if i - 1 >= 0 and self.visited.get((i - 1, j), False) is False:
                self.visited[(i - 1, j)] = True
                result += self.dfs(i - 1, j, visiteds + 1)
                self.visited[(i - 1, j)] = False
            if i + 1 < self.m and self.visited.get((i + 1, j), False) is False:
                self.visited[(i + 1, j)] = True
                result += self.dfs(i + 1, j, visiteds + 1)
                self.visited[(i + 1, j)] = False
            if j - 1 >= 0 and self.visited.get((i, j - 1), False) is False:
                self.visited[(i, j - 1)] = True
                result += self.dfs(i, j - 1, visiteds + 1)
                self.visited[(i, j - 1)] = False
            if j + 1 < self.n and self.visited.get((i, j + 1), False) is False:
                self.visited[(i, j + 1)] = True
                result += self.dfs(i, j + 1, visiteds + 1)
                self.visited[(i, j + 1)] = False
            return result
