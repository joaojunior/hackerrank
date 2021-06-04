from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = {}
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                counter = self.visit(i, j)
                if counter > 0:
                    result += 1
        return result

    def visit(self, i: int, j: int) -> int:
        if i >= 0 and i < self.m and j >= 0 and j < self.n:
            if self.grid[i][j] == "0" or self.visited.get((i, j), False):
                return 0
            else:
                self.visited[(i, j)] = True
                return (
                    1 +
                    self.visit(i-1, j) +
                    self.visit(i+1, j) +
                    self.visit(i, j-1) +
                    self.visit(i, j+1)
                )
        else:
            return 0
