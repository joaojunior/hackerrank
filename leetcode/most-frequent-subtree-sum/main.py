from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_frequent_tree_sum(self, root: TreeNode) -> List[int]:
        self.sums = {}
        self.max_ = 0
        self.post_order(root, 0)
        result = []
        for key, frequency in self.sums.items():
            if frequency == self.max_:
                result.append(key)
        return result

    def post_order(self, root, sum_):
        if root is not None:
            sum_left = self.post_order(root.left, sum_)
            sum_right = self.post_order(root.right, sum_)

            sum_ = root.val + sum_left + sum_right
            frequency = self.sums.get(sum_, 0) + 1
            self.sums[sum_] = frequency

            if frequency > self.max_:
                self.max_ = frequency
            return sum_
        return sum_
