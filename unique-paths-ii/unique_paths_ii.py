from typing import List


class Solution:
    def unique_paths_with_obstacles(self,
                                    obstacle_grid: List[List[int]]) -> int:
        self.memoization = {}
        return self.dfs(obstacle_grid, 0, 0)

    def dfs(self, obstacle_grid: List[List[int]], i: int, j: int) -> int:
        if (i, j) in self.memoization:
            return self.memoization[(i, j)]
        elif obstacle_grid[i][j] == 1:
            return 0
        elif i == len(obstacle_grid) - 1 and j == len(obstacle_grid[0]) - 1:
            return 1
        else:
            result = 0
            if i + 1 < len(obstacle_grid):
                result += self.dfs(obstacle_grid, i+1, j)
            if j + 1 < len(obstacle_grid[0]):
                result += self.dfs(obstacle_grid, i, j+1)
            self.memoization[(i, j)] = result
            return result
