class MaxSum():
    def max_sum(self, b):
        self.best = 0
        self.b = b
        if len(b) > 1:
            self.a = [0] * len(b)
            self._max_sum(0)
        return self.best

    def _max_sum(self, i):
        if i == len(self.b):
            sum_ = verify_sum(self.a)
            if sum_ > self.best:
                self.best = sum_
        else:
            self.a[i] = 1
            self._max_sum(i + 1)
            self.a[i] = self.b[i]
            self._max_sum(i + 1)


def verify_sum(arr):
    sum_ = 0
    for i in range(1, len(arr)):
        sum_ += abs(arr[i] - arr[i - 1])
    return sum_


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        max_sum = MaxSum()
        result = max_sum.max_sum(arr)
        print(result)
