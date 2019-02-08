from typing import List


class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        for i, value_i in enumerate(nums):
            for j, value_j in enumerate(nums[i+1:]):
                if value_i < value_j:
                    for k, value_k in enumerate(nums[i+j+1:]):
                        if value_j < value_k:
                            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 1, 5, 0, 3]
    print(solution.increasing_triplet(nums))
