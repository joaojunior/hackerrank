from typing import List


class Solution:
    def combination_sum(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        self.candidates = candidates
        self.size = len(candidates)
        self.target = target
        self.result = []
        for i in range(self.size):
            self.combination(i, [self.candidates[i]], self.candidates[i])
        return self.result

    def combination(self, i: int, numbers:  List[int], sum_: int):
        if sum_ == self.target:
            self.result.append(numbers[:])
        elif i < self.size and sum_ < self.target:
            self.combination(i, numbers[:] + [self.candidates[i]],
                             sum_ + self.candidates[i])
            self.combination(i+1, numbers[:], sum_)
