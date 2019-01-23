class ArithmeticExpression():
    def find(self, array):
        self.array = array
        self.size = len(array)
        queue = [(array[0], str(array[0]))]
        start = 0
        i = 1
        cache = {array[0]: True}
        while i < self.size:
            end = len(queue)
            j = start
            while j < end:
                sum_, response = queue[j]
                sum_plus = sum_ + array[i]
                sum_times = sum_ * array[i]
                sum_minus = sum_ - array[i]
                if sum_ % 101 == 0:
                    queue = [[sum_times, response + '*' + str(array[i])]]
                    j = 0
                    end = 0
                else:
                    if sum_plus not in cache:
                        queue.append(
                            [sum_plus, response + '+' + str(array[i])]
                        )
                        cache[sum_plus] = True
                    if sum_times not in cache:
                        queue.append(
                            [sum_times, response + '*' + str(array[i])]
                        )
                        cache[sum_times] = True
                    if sum_minus not in cache:
                        queue.append(
                            [sum_minus, response + '-' + str(array[i])]
                        )
                        cache[sum_minus] = True
                j += 1
            start = end
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
