from typing import List


class Solution:
    def find_target_sum_ways(self, nums: List[int], S: int) -> int:
        self.nums = nums
        self.size = len(nums)
        self.S = S
        self.memoize = {}

        return self.find(0, 0)

    def find(self, i: int, sum_: int) -> int:
        if i == self.size:
            if sum_ == self.S:
                return 1
            else:
                return 0
        else:
            if (i, sum_) in self.memoize:
                return self.memoize[(i, sum_)]
            else:
                add = self.find(i+1, sum_+self.nums[i])
                sub = self.find(i+1, sum_-self.nums[i])
                self.memoize[(i, sum_)] = add + sub
                return add + sub
