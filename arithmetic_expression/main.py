class ArithmeticExpression():
    def find(self, array):
        self.array = array
        self.size = len(array)

        result = self._find(1, array[0], [])
        response = str(array[0])
        for i, operator in enumerate(result):
            response += '{0}{1}'.format(operator, array[i+1])
        return response

    def _find(self, i, sum_, response):
        if i < self.size:
            result = (
                self._find(i+1, sum_ + self.array[i], response[:] + ['+']) or
                self._find(i+1, sum_ * self.array[i], response[:] + ['*']) or
                self._find(i+1, sum_ - self.array[i], response[:] + ['-']))
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
