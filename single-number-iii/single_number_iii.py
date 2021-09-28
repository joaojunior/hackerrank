from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        result = []
        for num, qty in counter.items():
            if qty == 1:
                result.append(num)
        return result
