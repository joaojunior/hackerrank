from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def path_sum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        self.result = []
        self.sum_ = sum_
        if root:
            self.search(root.val, [root.val], root)
        return self.result

    def search(self, sum_: int, numbers: List[int], root: TreeNode):
        if root is not None:
            if root.left is not None:
                left = root.left
                if sum_ + left.val == self.sum_ and self.is_leaf(left):
                    self.result.append(numbers[:]+[left.val])
                else:
                    self.search(sum_+left.val, numbers[:]+[left.val], left)
            if root.right is not None:
                right = root.right
                if sum_ + right.val == self.sum_ and self.is_leaf(right):
                    self.result.append(numbers[:]+[right.val])
                else:
                    self.search(sum_+right.val, numbers[:]+[right.val], right)
            if sum_ == self.sum_ and self.is_leaf(root):
                self.result.append(numbers[:])

    def is_leaf(self, root: TreeNode) -> bool:
        return root.left is None and root.right is None
