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
        return self.find(0, self.sets)

    def find(self, i, sets):
        if i == self.size:
            result = True
            for key, sum_ in sets.items():
                if sum_ != self.sum_:
                    result = False
            return result
        else:
            s = 0
            find = False
            while s < len(sets.keys()) and find is False:
                if sets[s] + self.nums[i] <= self.sum_:
                    new_sets = sets.copy()
                    new_sets[s] += self.nums[i]
                    find = self.find(i + 1, new_sets)
                s += 1
            return find


if __name__ == '__main__':
    nums = [3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932,
            4037, 2646, 3871, 269]
    k = 5
    s = Solution()
    print(s.can_partition_k_subsets(nums, k))
