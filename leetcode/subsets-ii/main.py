from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        queue = []
        size = len(nums)

        for i, num in enumerate(nums):
            if [num] not in result:
                result.append([num])
            queue.append((i, [num]))
        while queue:
            last, subset = queue.pop(0)
            for i in range(last + 1, size):
                new_subset = subset[:]
                new_subset.append(nums[i])
                new_subset = sorted(new_subset)
                if new_subset not in result:
                    result.append(new_subset[:])
                queue.append((i, new_subset))
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsets(nums))
