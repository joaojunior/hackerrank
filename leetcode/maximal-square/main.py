from typing import List


class Solution:
    def maximal_square(self, matrix: List[List[str]]) -> int:
        dp = {(0, 0): 0}
        max_size = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != '0':
                    dp[(i, j)] = min(
                        dp.get((i-1, j), 0), dp.get((i-1, j-1), 0),
                        dp.get((i, j-1), 0)
                    ) + 1
                    if dp[(i, j)] > max_size:
                        max_size = dp[(i, j)]
        return max_size * max_size
