from typing import List, Set, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> Set[Tuple[int]]:
        self.candidates = candidates
        self.size = len(candidates)
        self.target = target
        self.result = set()
        self.combination(0, [], 0)
        return self.result

    def combination(self, i: int, numbers:  List[int], sum_: int):
        if sum_ == self.target:
            self.result.add(tuple(sorted(numbers)))
        elif i < self.size and sum_ < self.target:
            self.combination(i+1, numbers[:] + [self.candidates[i]],
                             sum_ + self.candidates[i])
            self.combination(i+1, numbers[:], sum_)
