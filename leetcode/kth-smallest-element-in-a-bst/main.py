class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        self.i = 0
        self.k = k
        return self.in_order(root)

    def in_order(self, root):
        if root is not None:
            result = self.in_order(root.left)
            if result is not None:
                return result

            self.i += 1
            if self.i == self.k:
                return root.val

            result = self.in_order(root.right)
            if result is not None:
                return result
