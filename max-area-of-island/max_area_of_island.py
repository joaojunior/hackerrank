from typing import List


class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(self.grid)
        self.n = len(self.grid[0])
        max_ = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    count = self.count_island(i, j)
                    if count >= max_:
                        max_ = count
        return max_

    def count_island(self, row: int, col: int) -> int:
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return 0
        if self.grid[row][col] == 0:
            return 0
        else:
            self.grid[row][col] = 0
            return 1 + (
                self.count_island(row-1, col) +
                self.count_island(row+1, col) +
                self.count_island(row, col-1) +
                self.count_island(row, col+1)
            )
