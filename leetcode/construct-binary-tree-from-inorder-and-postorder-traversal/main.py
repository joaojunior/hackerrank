from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = None
        if postorder:
            val = postorder.pop()
            root = TreeNode(val)
            inorder_index = inorder.index(val)
            if inorder_index > 0:
                root.left = self.build_tree(
                    inorder[:inorder_index], postorder[:inorder_index])
            if inorder_index < len(inorder) - 1:
                root.right = self.build_tree(
                    inorder[inorder_index+1:], postorder[inorder_index:])
        return root
