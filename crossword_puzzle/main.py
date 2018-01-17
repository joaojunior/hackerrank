from collection import defaultdict
from copy import deep_copy


class Backtrack():
    def backtrack(self, words, matrix):
        self.words = words
        self.matrix = matrix
        self.size = len(self.matrix)
        self.calculate_possibles()

    def calculate_possibles(self):
        self.possibles = {}
        possibles = (self.calculate_possibles_horizontal() +
                     self.calculate_possibles_vertical())
        for word in self.words:
            self.possibles[word] = possibles[len(word)]

    def calculate_possibles_horizontal(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            quantity = 0
            col = None
            for j in range(self.size):
                if self.matrix[i][j] == '-':
                    quantity += 1
                    if col is None:
                        col = j
            if quantity > 1:
                possibles[quantity].append((i, col, 'H'))
        return possibles

    def calculate_possibles_vertical(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            quantity = 0
            row = None
            for j in range(self.size):
                if self.matrix[j][i] == '-':
                    quantity += 1
                    if row is None:
                        row = j
            if quantity > 1:
                possibles[quantity].append((row, i, 'V'))
        return possibles

    def try_fill(self, matrix, word, position):
        new_matrix = deep_copy(matrix)
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
