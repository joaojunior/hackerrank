from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.preorder(root)
        return self.result

    def preorder(self, root):
        if root is not None:
            self.result.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
