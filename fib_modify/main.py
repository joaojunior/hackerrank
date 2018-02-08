class FibonacciModified:
    def fibonacci_modified(self, t1, t2, n):
        self.memoize = {}
        self.t1 = t1
        self.t2 = t2
        return self.calculate(n)

    def calculate(self, n):
        if n == 1:
            return self.t1
        elif n == 2:
            return self.t2
        else:
            if n in self.memoize:
                return self.memoize[n]
            self.memoize[n] = (self.calculate(n - 1) ** 2 +
                               self.calculate(n - 2))
            return self.memoize[n]


if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    f = FibonacciModified()
    result = f.fibonacci_modified(t1, t2, n)
    print(result)
