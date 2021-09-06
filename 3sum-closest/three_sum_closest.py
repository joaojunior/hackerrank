from typing import List


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        max_distance = 1000
        result = 0
        for i in range(size - 2):
            left = i + 1
            r = size - 1
            while left < r:
                sum_ = nums[i] + nums[left] + nums[r]
                distance = abs(sum_ - target)
                if distance < max_distance:
                    max_distance = distance
                    result = sum_
                if sum_ > target:
                    r -= 1
                elif sum_ < target:
                    left += 1
                else:
                    return result
        return result
