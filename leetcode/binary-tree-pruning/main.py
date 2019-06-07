class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def prune_tree(self, root: TreeNode) -> TreeNode:
        self.post_order(root)
        return root

    def post_order(self, root) -> bool:
        if root is not None:
            left = self.post_order(root.left)
            right = self.post_order(root.right)
            if left is False:
                root.left = None
            if right is False:
                root.right = None
            if left is False and right is False:
                return root.val == 1
            else:
                return True
        else:
            return False
