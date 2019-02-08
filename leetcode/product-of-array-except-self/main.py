from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        result = []
        memoize = {}
        for i, num1 in enumerate(nums):
            multi = 1
            if num1 not in memoize:
                for j, num2 in enumerate(nums):
                    if i != j:
                        multi *= num2
                memoize[num1] = multi
            result.append(memoize[num1])
        return result
