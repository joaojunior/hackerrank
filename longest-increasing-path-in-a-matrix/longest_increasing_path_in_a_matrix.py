from typing import List


class Solution:
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.result = 0
        self.memoization = {}
        for i in range(self.m):
            for j in range(self.n):
                result = self.find_longest_from(i, j)
                if result > self.result:
                    self.result = result
        return self.result

    def find_longest_from(self, i: int, j: int) -> int:
        if (i, j) in self.memoization:
            return self.memoization[(i, j)]
        elif i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 0
        else:
            result = 1
            if i - 1 >= 0 and self.matrix[i-1][j] > self.matrix[i][j]:
                result = max(result, 1 + self.find_longest_from(i-1, j))
            if i + 1 < self.m and self.matrix[i+1][j] > self.matrix[i][j]:
                result = max(result, 1 + self.find_longest_from(i+1, j))
            if j - 1 >= 0 and self.matrix[i][j-1] > self.matrix[i][j]:
                result = max(result, 1 + self.find_longest_from(i, j-1))
            if j + 1 < self.n and self.matrix[i][j+1] > self.matrix[i][j]:
                result = max(result, 1 + self.find_longest_from(i, j+1))
            self.memoization[(i, j)] = result
            return result
