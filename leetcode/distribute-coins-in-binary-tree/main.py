class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distribute_coins(self, root: TreeNode) -> int:
        self.result = 0
        self.post_order(root)
        return self.result

    def post_order(self, root) -> int:
        if root is not None:
            left = self.post_order(root.left)
            right = self.post_order(root.right)
            val = left + right + root.val - 1
            self.result += abs(val)
            return val
        return 0
