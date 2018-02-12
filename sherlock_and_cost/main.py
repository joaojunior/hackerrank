class MaxSum():
    def max_sum(self, b):
        self.b = b
        self.a = [0] * len(b)
        self.memoize = {}
        return self._max_sum(len(b) - 1, max(b))

    def _max_sum(self, i, last):
        if i in self.memoize:
            return self.memoize[i]
        if i == 0:
            if abs(last - 1) > abs(last - self.b[0]):
                self.a[0] = 1
            else:
                self.a[0] = self.b[0]
            self.memoize[0] = self.a[0]
            return self.a[0]
        else:
            if (abs(1 - self._max_sum(i - 1, 1)) >
                    abs(self.b[i] - self._max_sum(i - 1, self.b[i]))):
                self.a[i] = 1
            else:
                self.a[i] = self.b[i]
            self.memoize[i] = self.a[i]
            return self.a[i]


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
        print(arr, len(arr))
        print(max_sum.a, len(max_sum.a), verify_sum(max_sum.a))
