from typing import List


class Solution:
    def update_board(self, board: List[List[str]],
                     click: List[int]) -> List[List[str]]:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self._update_board(click[0], click[1])
        return self.board

    def _update_board(self, i: int, j: int):
        if i >= 0 and i < self.m and j >= 0 and j < self.n:
            if self.board[i][j] == 'M':
                self.board[i][j] = 'X'
            elif self.board[i][j] == 'E':
                mines = self.count_mines(i, j)
                if mines == 0:
                    self.board[i][j] = 'B'
                    self._update_board(i-1, j-1)
                    self._update_board(i-1, j)
                    self._update_board(i-1, j+1)
                    self._update_board(i, j-1)
                    self._update_board(i, j+1)
                    self._update_board(i+1, j-1)
                    self._update_board(i+1, j)
                    self._update_board(i+1, j+1)
                else:
                    self.board[i][j] = str(mines)

    def count_mines(self, i: int, j: int) -> int:
        mines = 0
        bombs = ['M', 'X']
        if i - 1 >= 0:
            if j - 1 >= 0 and self.board[i - 1][j - 1] in bombs:
                mines += 1
            if self.board[i - 1][j] in bombs:
                mines += 1
            if j + 1 < self.n and self.board[i - 1][j + 1] in bombs:
                mines += 1
        if j - 1 >= 0 and self.board[i][j - 1] in bombs:
            mines += 1
        if j + 1 < self.n and self.board[i][j + 1] in bombs:
            mines += 1
        if i + 1 < self.m:
            if j - 1 >= 0 and self.board[i + 1][j - 1] in bombs:
                mines += 1
            if self.board[i + 1][j] in bombs:
                mines += 1
            if j + 1 < self.n and self.board[i + 1][j + 1] in bombs:
                mines += 1
        return mines
