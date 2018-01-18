from collections import defaultdict
from copy import deepcopy


class Backtrack():
    def backtrack(self, words, matrix):
        self.words = words
        self.matrix = deepcopy(matrix)
        self.size = len(self.matrix)
        self.calculate_possibles()
        self.quantity = len(words)
        i = 0
        possibles = []
        while len(possibles) == 0:
            word = self.words[i]
            possibles = self.possibles.get(word, [])
            i += 1
        for possible in possibles:
            new_matrix, result = self.try_fill(matrix,
                                               word,
                                               possible)
            result = self._backtrack([possible], [word], new_matrix)
            if result is not None:
                return result

    def _backtrack(self, filled, words, matrix):
        if len(words) == self.quantity:
            print_matrix(matrix)
            return matrix
        else:
            for word in self.words:
                if word not in words:
                    for possible in self.possibles[word]:
                        if possible not in filled:
                            new_matrix = deepcopy(matrix)
                            new_matrix, result = self.try_fill(new_matrix,
                                                               word,
                                                               possible)
                            if result:
                                new_filled = filled[:]
                                new_words = words[:]
                                new_filled.append(possible)
                                new_words.append(word)
                                result = self._backtrack(new_filled,
                                                         new_words,
                                                         new_matrix)
                                if result is not None:
                                    return new_matrix

    def calculate_possibles(self):
        self.possibles = {}
        possibles_horizontal = self.calculate_possibles_horizontal()
        possibles_vertical = self.calculate_possibles_vertical()
        for word in self.words:
            self.possibles[word] = (possibles_horizontal[len(word)] +
                                    possibles_vertical[len(word)])

    def calculate_possibles_horizontal(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            row = self.matrix[i]
            j = 0
            while j < self.size - 1 and row[j] + row[j + 1] != '--':
                j += 1
            begin = j
            j = self.size - 1
            while j > 0 and row[j] + row[j - 1] != '--':
                j -= 1
            end = j
            if begin < self.size - 1 and end > 0:
                size = end - begin + 1
                possibles[size].append((i, begin, 'H'))
        return possibles

    def calculate_possibles_vertical(self):
        possibles = defaultdict(list)
        for i in range(self.size):
            j = 0
            while (j < self.size - 1 and
                    self.matrix[j][i] + self.matrix[j+1][i] != '--'):
                    j += 1
            begin = j
            j = self.size - 1
            while j > 0 and self.matrix[j][i] + self.matrix[j-1][i] != '--':
                    j -= 1
            end = j
            if begin < self.size - 1 and end > 0:
                size = end - begin + 1
                possibles[size].append((begin, i, 'V'))
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
                return deepcopy(matrix), False
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
    result = backtrack.backtrack(words, matrix)
