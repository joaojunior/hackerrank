from typing import List


class Solution():
    def min_sub_array_len(self, s: int, nums: List[int]) -> int:
        size = 0
        i = 0
        sum_ = 0
        j = i - 1
        while i < len(nums):
            while (j < len(nums) - 1 and sum_ < s and
                   (size == 0 or j - i + 1 < size)):
                j += 1
                sum_ += nums[j]
            if (size == 0 or j - i + 1 < size) and sum_ >= s:
                size = j - i + 1
            sum_ -= nums[i]
            i += 1
        return size
