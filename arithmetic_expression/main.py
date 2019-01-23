class ArithmeticExpression():
    def find(self, array):
        self.array = array
        self.size = len(array)
        queue = [(array[0], str(array[0]))]
        i = 1
        while i < self.size:
            q = []
            for j in range(len(queue)):
                sum_, response = queue[j]
                sum_plus = sum_ + array[i]
                sum_times = sum_ * array[i]
                sum_minus = sum_ - array[i]
                if sum_ % 101 == 0:
                    q = [[sum_times, response + '*' + str(array[i])]]
                    break
                else:
                    q.append([sum_plus, response + '+' + str(array[i])])
                    q.append([sum_times, response + '*' + str(array[i])])
                    q.append([sum_minus, response + '-' + str(array[i])])
            queue = q[:]
            i += 1
        for sum_, response in queue:
            if sum_ % 101 == 0:
                return response

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
