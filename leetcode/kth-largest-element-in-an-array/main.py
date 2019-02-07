from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]
