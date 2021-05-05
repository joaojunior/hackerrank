from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.qty = len(nums) - 1
        self.result = []
        self.generate_permuation(0)
        return self.result

    def generate_permuation(self, i):
        if i == self.qty:
            self.result.append(self.nums[:])
        else:
            for j in range(i, self.qty + 1):
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                self.generate_permuation(i+1)
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
