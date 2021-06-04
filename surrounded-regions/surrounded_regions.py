from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.visited = {}
        for i in [0, self.m - 1]:
            for j in range(self.n):
                self.visiting(i, j)
        for i in range(self.m):
            for j in [0, self.n - 1]:
                self.visiting(i, j)
        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                if self.visited.get((i, j), False) is False:
                    self.board[i][j] = 'X'

    def visiting(self, i, j):
        if self.in_boudering(i, j):
            if (self.visited.get((i, j), False) is False and
                    self.board[i][j] == 'O'):
                self.visited[(i, j)] = True
                self.visiting(i-1, j)
                self.visiting(i+1, j)
                self.visiting(i, j-1)
                self.visiting(i, j+1)

    def in_boudering(self, i, j):
        return i >= 0 and i < self.m and j >= 0 and j < self.n
