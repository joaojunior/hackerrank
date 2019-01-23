class ArithmeticExpression():
    def find(self, array):
        self.array = array
        self.size = len(array)

        result = self._find(1, array[0], str(array[0]))
        return result

    def _find(self, i, sum_, response):
        if i < self.size:
            value = self.array[i]
            if sum_ % 101 == 0:
                return self._find(
                    i+1, sum_ * self.array[i], response + '*' + str(value)
                )
            result = (
                self._find(i+1, sum_ + value, response + '+' + str(value)) or
                self._find(i+1, sum_ * value, response + '*' + str(value)) or
                self._find(i+1, sum_ - value, response + '-' + str(value)))
            return result
        else:
            if sum_ % 101 == 0:
                return response
            else:
                return False


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    a = ArithmeticExpression()
    print(a.find(numbers))
