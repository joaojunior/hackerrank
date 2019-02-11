import heapq
from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        max_ = 0
        last = -99
        qty = 0
        while nums:
            i = heapq.heappop(nums)
            if i - 1 == last:
                qty += 1
                last = i
                max_ = max(max_, qty)
            elif i != last:
                qty = 1
                last = i
                max_ = max(max_, 1)
        return max_
