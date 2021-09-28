from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> List[int]:
        size = len(nums)
        times = size // 3
        counter = {}
        result = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num, qty in counter.items():
            if qty > times:
                result.append(num)
        return result
