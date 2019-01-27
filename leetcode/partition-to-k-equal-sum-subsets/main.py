from typing import List


class Solution:
    def can_partition_k_subsets(self, nums: List[int], k: int) -> bool:
        self.nums = nums
        self.size = len(nums)
        self.k = k
        self.sum_ = sum(nums) / k
        self.sets = {}
        for i in range(k):
            self.sets[i] = 0
        return self.find(0)

    def find(self, i):
        if i == self.size:
            result = True
            for key, sum_ in self.sets.items():
                if sum_ != self.sum_:
                    result = False
            return result
        else:
            s = 0
            find = False
            while s < len(self.sets.keys()) and find is False:
                if self.sets[s] + self.nums[i] <= self.sum_:
                    self.sets[s] += self.nums[i]
                    find = True
                s += 1
            if find is True:
                return self.find(i + 1)
            else:
                return False


if __name__ == '__main__':
    nums = [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]
    k = 3
    s = Solution()
    print(s.can_partition_k_subsets(nums, k))
