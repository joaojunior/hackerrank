from typing import List


class Solution:
    def combination_sum_3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.result = []
        self.combination(1, [])
        return self.result

    def combination(self, i: int, numbers: List[int], qty: int = 0):
        if qty == self.k:
            if sum(numbers) == self.n:
                self.result.append(numbers)
        elif i <= 9:
            if sum(numbers) + i <= self.n:
                self.combination(i+1, numbers[:] + [i], qty + 1)
            self.combination(i+1, numbers[:], qty)
        pass
