import sys

sys.setrecursionlimit(10**4)


class Backtrack():
    def backtrack(self, n, divisors):
        self.divisors = sorted(divisors)
        self.memoize = {}
        return self._backtrack(n)

    def _backtrack(self, n):
        if n in self.memoize:
            return self.memoize[n]
        temp_max = 0
        for divisor in self.divisors:
            if divisor < n and n % divisor == 0:
                temp_max = max(1 + (n//divisor) *
                               self._backtrack(divisor), temp_max)
        self.memoize[n] = temp_max
        return self.memoize[n]


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n, m = input().split()
        n = int(n)
        m = int(m)
        _divisors = input().split()
        divisors = []
        for divisor in _divisors:
            divisors.append(int(divisor))
        backtrack = Backtrack()
        print(backtrack.backtrack(n, divisors))
