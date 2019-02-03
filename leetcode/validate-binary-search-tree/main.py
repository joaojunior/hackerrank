import sys


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_valid_BST(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        result = True
        if root.left is not None:
            if root.val > root.left.val:
                result = self.is_valid(root.left, -sys.maxsize, root.val)
            else:
                result = False
        if result is False:
            return False
        if root.right is not None:
            if root.val < root.right.val:
                result = self.is_valid(root.right, root.val, sys.maxsize)
            else:
                result = False
        return result

    def is_valid(self, root, min_, max_):
        result = True
        if root.left is not None:
            if min_ < root.left.val < max_ and root.left.val < root.val:
                result = self.is_valid(root.left, min_, root.val)
            else:
                result = False
        if result is True and root.right is not None:
            if min_ < root.right.val < max_ and root.right.val > root.val:
                result = self.is_valid(root.right, root.val, max_)
            else:
                result = False
        return result
