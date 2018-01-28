class MaxSumArray():
    def max_sum_array(self, array):
        self.max_ = max(array)
        self.array = array
        self.size = len(array)
        self.memoize_max = {}
        self.memoize_min = {}
        self._max_sum_array(0, self.size - 1)
        result = 0
        for i in range(self.size):
            for j in range(self.size - 1, i, -1):
                for k in range(j + 1, self.size):
                    for l in range(self.size-1, k, -1):
                        r = self._max_abs_sum(i, j, k, l)
                        if r > result:
                            result = r
        return result

    def _max_abs_sum(self, i, j, k, l):
        return max(abs(self.memoize_max[(i, j)] - self.memoize_max[(k, l)]),
                   abs(self.memoize_max[(i, j)] - self.memoize_min[(k, l)]),
                   abs(self.memoize_min[(i, j)] - self.memoize_max[(k, l)]),
                   abs(self.memoize_min[(i, j)] - self.memoize_min[(k, l)]))

    def _max_sum_array(self, i, j):
        if i > j:
            return -abs(self.max_ * self.size), abs(self.max_ * self.size)
        else:
            if (i, j) in self.memoize_max:
                return self.memoize_max[(i, j)], self.memoize_min[(i, j)]
            else:
                results = (self._max_sum_array(i, j-1),
                           self._max_sum_array(i+1, j),
                           self._max_sum_array(i+1, j-1))
                max_ = sum(self.array[i:j+1])
                min_ = max_
                for result in results:
                    if result[0] > max_:
                        max_ = result[0]
                    if result[1] < min_:
                        min_ = result[1]
                self.memoize_max[(i, j)] = max_
                self.memoize_min[(i, j)] = min_
                return max_, min_


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        size = int(input())
        numbers_raw = input().split()
        numbers = []
        for number in numbers_raw:
            numbers.append(int(number))
        m = MaxSumArray()
        print(m.max_sum_array(numbers))
