class Backtrack():
    def backtrack(self, n, x):
        self.n = n
        self.x = x
        self.max = int(n ** (1 / x))
        self.quantity = 0
        for i in range(1, self.max + 1):
            self._backtrack(i, i ** x)
        print(self.quantity)

    def _backtrack(self, number, sum_):
        if sum_ == self.n:
            self.quantity += 1
        else:
            for i in range(number + 1, self.max + 1):
                power = i ** self.x
                if power + sum_ <= self.n:
                    self._backtrack(i, sum_ + power)


if __name__ == '__main__':
    n = int(input())
    x = int(input())
    backtrack = Backtrack()
    backtrack.backtrack(n, x)
