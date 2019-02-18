from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.postorder(root)
        return self.result

    def postorder(self, root: TreeNode):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.result.append(root.val)
