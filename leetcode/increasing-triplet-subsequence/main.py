from typing import List


class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        k = 2
        while i < len(nums) - 2 and j < len(nums) - 1:
            if nums[i] < nums[j]:
                if nums[j] < nums[k]:
                    return True
                else:
                    k += 1
                    if k == len(nums):
                        j += 1
                        k = j + 1
            else:
                j += 1
                k = j + 1
                if j == len(nums) or k == len(nums):
                    i += 1
                    j = i + 1
                    k = j + 1
        return False
