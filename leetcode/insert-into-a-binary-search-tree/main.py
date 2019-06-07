class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insert_into_BST(self, root: TreeNode, val: int) -> TreeNode:
        parent = None
        current = root
        while current is not None:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root
