from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        total = 1
        i = 1
        size = len(nums)
        qty = 1
        while total < size:
            if nums[i] == nums[i - 1]:
                qty += 1
                if qty > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                i += 1
                qty = 1
            total += 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.remove_duplicates(nums))
