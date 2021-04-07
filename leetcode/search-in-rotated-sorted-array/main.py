from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.binary_search(0, len(nums) - 1, target)

    def binary_search(self, l: int, r: int, value: int) -> int:  # noqa
        if l > r:
            return -1
        else:
            mid = (l + r) // 2
            if self.nums[mid] == value:
                return mid
            elif value < self.nums[mid]:
                result = self.binary_search(l, mid-1, value)
                if result == -1:
                    return self.binary_search(mid+1, r, value)
                else:
                    return result
            else:
                result = self.binary_search(mid+1, r, value)
                if result == -1:
                    return self.binary_search(l, mid-1, value)
                else:
                    return result
