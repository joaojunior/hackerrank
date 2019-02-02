from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        finded = False
        i = 0
        j = 0
        self.board = board
        self.size = len(self.board)
        self.word = word
        while finded is False and i < self.size and j < len(self.board[i]):
            if board[i][j] == word[0]:
                finded = self.find(i, j, 1, [(i, j)])
            j += 1
            if j == len(self.board[i]):
                j = 0
                i += 1
        return finded

    def find(self, i, j, k, used):
        if k == len(self.word):
            return True
        else:
            r = False
            if (i, j+1) not in used and self.verify_position(i, j+1, k, r):
                new_used = used[:]
                new_used.append((i, j+1))
                r = self.find(i, j+1, k+1, new_used)
            if (i, j-1) not in used and self.verify_position(i, j-1, k, r):
                new_used = used[:]
                new_used.append((i, j-1))
                r = self.find(i, j-1, k+1, new_used)
            if (i+1, j) not in used and self.verify_position(i+1, j, k, r):
                new_used = used[:]
                new_used.append((i+1, j))
                r = self.find(i+1, j, k+1, new_used)
            if (i-1, j) not in used and self.verify_position(i-1, j, k, r):
                new_used = used[:]
                new_used.append((i-1, j))
                r = self.find(i-1, j, k+1, new_used)
            return r

    def verify_position(self, i, j, k, result):
        return (
            (result is False) and
            (-1 < i < self.size) and
            (-1 < j < len(self.board[i])) and
            (self.word[k] == self.board[i][j])
        )


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ESCEZDAF'
    print(solution.exist(board, word))
