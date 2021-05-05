from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.n = n
        self.k = k
        self.current_combination = []
        self.generate_combination(1)
        return self.result

    def generate_combination(self, i: int):
        if len(self.current_combination) == self.k:
            self.result.append(self.current_combination[:])
        else:
            for j in range(i, self.n+1):
                self.current_combination.append(j)
                self.generate_combination(j+1)
                self.current_combination.pop()
