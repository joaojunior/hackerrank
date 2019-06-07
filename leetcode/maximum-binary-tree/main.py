from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def construct_maximum_binary_tree(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self._create_max_binary_tree(0, len(nums) - 1)

    def _create_max_binary_tree(self, start, end):
        if end < start:
            return None
        else:
            largest = self._find_max(start, end)
            p = TreeNode(self.nums[largest])
            p.left = self._create_max_binary_tree(start, largest - 1)
            p.right = self._create_max_binary_tree(largest + 1, end)
            return p

    def _find_max(self, start, end):
        largest = start
        for i in range(start, end + 1):
            if self.nums[i] > self.nums[largest]:
                largest = i
        return largest
