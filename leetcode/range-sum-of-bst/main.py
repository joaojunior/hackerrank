class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def range_sum_BST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        else:
            if L <= root.val <= R:
                return root.val + (self.range_sum_BST(root.left, L, R) +
                                   self.range_sum_BST(root.right, L, R))
            elif R <= root.val:
                return self.range_sum_BST(root.left, L, R)
            elif L >= root.val:
                return self.range_sum_BST(root.right, L, R)
            else:
                return 0
