from typing import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        minimum = -float("inf")
        size = len(nums)
        nums.insert(0, minimum)
        nums.append(minimum)
        for i in range(size):
            i += 1
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i - 1
