class Backtrack():
    def backtrack(self, n):
        self.n = n
        self.max_b = 1
        self.max_c = 2
        self.caracters = ['a', 'b', 'c']
        self.quantity = 0
        self._backtrack(['a'], 0, 0)
        self._backtrack(['b'], 1, 0)
        self._backtrack(['c'], 0, 1)
        return self.quantity

    def _backtrack(self, word, quantity_b, quantity_c):
        if len(word) == self.n:
            self.quantity += 1
        else:
            self._backtrack(word[:] + ['a'], quantity_b, quantity_c)
            if quantity_b + 1 <= self.max_b:
                self._backtrack(word[:] + ['b'], quantity_b + 1, quantity_c)
            if quantity_c + 1 <= self.max_c:
                self._backtrack(word[:] + ['c'], quantity_b, quantity_c + 1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        backtrack = Backtrack()
        print(backtrack.backtrack(n))
