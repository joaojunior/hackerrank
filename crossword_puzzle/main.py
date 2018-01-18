from collections import defaultdict
from copy import deepcopy


class Backtrack():
    def backtrack(self, words, matrix):
        self.words = words
        self.matrix = matrix
        self.size = len(self.matrix)
        self.calculate_possibles()

    def calculate_possibles(self):
        self.possibles = {}
        possibles_horizontal = self.calculate_possibles_horizontal()
        possibles_vertical = self.calculate_possibles_vertical()
        for word in self.words:
            self.possibles[word] = (possibles_horizontal[len(word)] +
                                    possibles_vertical[len(word)])
        print(self.possibles)

    def calculate_possibles_horizontal(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            quantity = 0
            col = 0
            col_last = 0
            for j in range(self.size - 1):
                if self.matrix[i][j] == '-':
                    quantity += 1
                    col_last = j
                    if col == 0:
                        col = j
            if quantity > 1 and quantity == col_last - col + 1:
                possibles[quantity].append((i, col, 'H'))
        return possibles

    def calculate_possibles_vertical(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            quantity = 0
            row = 0
            row_last = 0
            for j in range(self.size):
                if self.matrix[j][i] == '-':
                    quantity += 1
                    row_last = j
                    if row is None:
                        row = j
            if quantity > 1 and quantity == row_last - row + 1:
                possibles[quantity].append((row, i, 'V'))
        return possibles

    def try_fill(self, matrix, word, position):
        new_matrix = deepcopy(matrix)
        row_started = position[0]
        col_started = position[1]
        direction = position[2]
        for j in range(len(word)):
            if direction == 'H':
                row = row_started
                col = col_started + j
            elif direction == 'V':
                row = row_started + j
                col = col_started
            if new_matrix[row][col] == word[j] or new_matrix[row][col] == '-':
                new_matrix[row][col] = word[j]
            else:
                return matrix, False
        return new_matrix, True


def print_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        print(''.join(matrix[i]))


if __name__ == "__main__":
    size = 10
    matrix = []
    for i in range(size):
        row = list(input())
        matrix.append(row[:])
    words = input().split(";")
    backtrack = Backtrack()
    backtrack.backtrack(words, matrix)
    print_matrix(matrix)
    print(words)
