class SherlockCost():
    def cost(self, b):
        self.b = b
        last = len(b) - 1
        self.memoize = {}
        return max(self._cost(1, last-1), self._cost(b[last], last-1))

    def _cost(self, previous, i):
        if (previous, i) in self.memoize:
            return self.memoize[(previous, i)]
        elif i == 0:
            self.memoize[(previous, i)] = max(abs(1 - previous),
                                              abs(self.b[0] - previous))
            return self.memoize[(previous, i)]
        else:
            result = max(self._cost(1, i - 1) + abs(1 - previous),
                         self._cost(self.b[i], i - 1) + abs(self.b[i]-previous)
                         )
            self.memoize[(previous, i)] = result
            return result


if __name__ == '__main__':
    sc = SherlockCost()
    b = [10, 1, 10, 1, 10]
    b = [4, 7, 9]
    print(sc.cost(b))
