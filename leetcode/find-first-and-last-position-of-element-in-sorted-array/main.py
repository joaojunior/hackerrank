from typing import List


class Solution():
    def search_range(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        return self.binary_search(0, len(nums)-1, target)

    def binary_search(self, left: int, right: int, target: int) -> List[int]:
        if left > right:
            return [-1, -1]
        else:
            mid = (right + left) // 2
            if self.nums[mid] == target:
                start = end = mid
                while start >= 0 and self.nums[start] == target:
                    start -= 1
                while end < len(self.nums) and self.nums[end] == target:
                    end += 1
                return [start+1, end-1]
            elif self.nums[mid] > target:
                return self.binary_search(left, mid - 1, target)
            else:
                return self.binary_search(mid + 1, right, target)
