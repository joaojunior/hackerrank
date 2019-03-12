class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def count_nodes(self, root: TreeNode) -> int:
        if root is not None:
            return (1 + self.count_nodes(root.left) +
                    self.count_nodes(root.right))
        else:
            return 0
