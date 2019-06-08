class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_ancestor_diff(self, root: TreeNode) -> int:
        return self.in_order(root, root.val, root.val)

    def in_order(self, root: TreeNode, min_: int, max_: int) -> int:
        if root is not None:
            new_min = min(min_, root.val)
            new_max = max(max_, root.val)
            return max(
                abs(root.val - min_),
                abs(root.val - max_),
                self.in_order(root.left, new_min, new_max),
                self.in_order(root.right, new_min, new_max)
            )
        return 0
