from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        self.nums = nums
        self.last = len(self.nums) - 1
        return self.search(0, self.last, self.nums[0])

    def search(self, left: int, right: int, target: int) -> int:
        if left > right:
            return target
        else:
            mid = (left + right) // 2
            if self.nums[mid] < target:
                if self.nums[mid-1] < self.nums[mid]:
                    return self.search(left, mid - 1, self.nums[mid-1])
                else:
                    return self.search(mid + 1, right, self.nums[mid])
            else:
                return self.search(mid + 1, right, target)
