from typing import List


class Solution:
    def sort_colors(self, nums: List[int]):
        frequency = {0: 0, 1: 0, 2: 0}
        for cor in nums:
            frequency[cor] += 1
        start = 0
        for cor, qty in frequency.items():
            for i in range(start, qty + start):
                nums[i] = cor
            start += qty
