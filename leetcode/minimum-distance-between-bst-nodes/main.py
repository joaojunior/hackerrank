class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def min_diff_in_BST(self, root: TreeNode) -> int:
        left = float('inf')
        right = float('inf')
        if root.left:
            left = min(abs(root.val - self.max(root.left)),
                       self.min_diff_in_BST(root.left))
        if root.right:
            right = min(abs(root.val - self.min(root.right)),
                        self.min_diff_in_BST(root.right))
        return min(left, right)

    def max(self, root):
        while root.right is not None:
            root = root.right
        return root.val

    def min(self, root):
        while root.left is not None:
            root = root.left
        return root.val
