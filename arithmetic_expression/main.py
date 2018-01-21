import sys
sys.setrecursionlimit(10**9)


class Backtrack():
    def backtrack(self, numbers, divisor=101):
        self.divisor = divisor
        self.numbers = numbers
        self.signals = ['*', '-', '+']
        self.size = len(numbers)
        self.find = False
        for signal in self.signals:
            if self.find is False:
                self._backtrack(0, [signal], numbers[0])

    def _backtrack(self, i, signals, sum_):
        if sum_ % self.divisor == 0:
            self.find = True
            j = 0
            while j < i:
                print(self.numbers[j], signals[j+1], sep='', end='')
                j += 1
            print(self.numbers[j], end='')
            sys.exit(0)
        else:
            if i < self.size - 1 and len(signals) <= 5 * self.size:
                for signal in self.signals:
                    if signal == '*':
                        new_sum = sum_ * self.numbers[i + 1]
                    elif signal == '-':
                        new_sum = sum_ - self.numbers[i + 1]
                    elif signal == '+':
                        new_sum = sum_ + self.numbers[i + 1]
                    if self.find is False:
                        self._backtrack(i + 1, signals[:] + [signal], new_sum)
                    else:
                        return


if __name__ == '__main__':
    n = int(input())
    numbers_raw = input().split()
    numbers = []
    for i in range(n):
        numbers.append(int(numbers_raw[i]))
    backtrack = Backtrack()
    backtrack.backtrack(numbers)
